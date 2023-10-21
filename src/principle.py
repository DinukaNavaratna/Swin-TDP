from flask_restful import Resource
from flask import request
import numpy as np
import pandas as pd
from pandas import read_excel
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import ftplib
import os
from dotenv import load_dotenv
from datetime import datetime
from loguru import logger
from faker import Faker
# ----------- Dashboard --------------------------------- 

load_dotenv()
WEB_HOST = os.getenv("WEB_HOST")
FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")
IMG_DIR = "files/img/"
PHP_DIR = "files/php/"

# data source
xlsxJan = pd.ExcelFile('resources/datasets/Student Survey - Jan.xlsx')
xlsxJuly = pd.ExcelFile('resources/datasets/Student Survey - July.xlsx')
        
#        request_body = request.json
#        survey = request_body["survey"]
#        
#        if(survey == "1"):
#            xlsx = xlsxJan
#            ftpSurvey = "s1/"
#        else:
#            xlsx = xlsxJuly
#            ftpSurvey = "s2/"
        

class generateImages(Resource):
    def post(self):
        
        request_body = request.json
        survey = request_body["survey"]
        
        if(survey == "1"):
            xlsx = xlsxJan
            ftpSurvey = "s1/"
        else:
            xlsx = xlsxJuly
            ftpSurvey = "s2/"
        
        f = open(PHP_DIR+"principle.php", "w")
        f.write("/*Created on "+datetime.now().strftime('%Y-%m-%d')+"*/\n")
        f.close()
        f = open(PHP_DIR+"principle.php", "a")

        # survey result  
        df_principal = read_excel(xlsx, sheet_name='responses')

        # students attributes
        df2_principal = read_excel(xlsx, sheet_name='participants')

        # inner merge on participant ID
        df3_principal = pd.merge(df_principal, df2_principal, on=['Participant-ID'])

        # data cleaning
        # select only 'completed'
        df3_principal = df3_principal[df3_principal['Status'].isin(['completed'])]
        
        
        ## Landing page

        print('Total student participants :', len(df3_principal))
        f.write("\n$total_student_participants = \""+str(len(df3_principal))+"\";")

        year = []
        for i in range (11):
            year.append(i)

        principal_landing_no_of_student_by_year = []
        for index in year:
            principal_landing_no_of_student_by_year.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'CompleteYears'].count())

        plt.bar(year, principal_landing_no_of_student_by_year)
        plt.xlabel('Years completed in the school')
        plt.ylabel('No. of student')
        plt.title('No. of student participated in the survey')
        plt.savefig(IMG_DIR+'img_'+'no_of_student_by_year'+'.png', dpi=500)
        f.write("\n$img_"+"no_of_student_by_year = \""+str(WEB_HOST+"img_"+"no_of_student_by_year"+".png")+"\";")
        plt.cla()
        
        
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

        principal_landing_no_of_student_by_house = []
        for index in house:
            principal_landing_no_of_student_by_house.append(df3_principal.loc[df3_principal['House'] == index, 'House'].count())

        plt.bar(house, principal_landing_no_of_student_by_house)
        plt.xlabel('House')
        plt.ylabel('No. of student')
        plt.title('No. of student participated in the survey')
        plt.savefig(IMG_DIR+'img_'+'no_of_student_by_house'+'.png', dpi=500)
        f.write("\n$img_"+"no_of_student_by_house = \""+str(WEB_HOST+"img_"+"no_of_student_by_house"+".png")+"\";")
        plt.cla()
        
        
        ## View by year
        ### 1. academic and attandance
        #### 1.1 What is their academic result and attandance?
        year = []
        for i in range (11):
            year.append(i)

        principal_year_attandance = []
        principal_year_academic = []
        for index in year:
            principal_year_attandance.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Attendance'].mean()) 
            principal_year_academic.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Perc_Academic'].mean()) 
            
        year_acad_n_att = np.transpose([principal_year_academic, principal_year_attandance])
        year_acad_n_att_plot = pd.DataFrame(year_acad_n_att, columns=['Academic', 'Attandance'])

        plot = year_acad_n_att_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('Academic result / attandance')
        plot.set_title('Average academic result and attandance')
        plt.savefig(IMG_DIR+'img_'+'average_academic_result_and_attendance'+'.png', dpi=500)
        f.write("\n$img_"+"average_academic_result_and_attendance = \""+str(WEB_HOST+"img_"+"average_academic_result_and_attendance"+".png")+"\";")
        plt.cla()
        

        #### 1.2 Which language does they speak?
        year = []
        for i in range (11):
            year.append(i)

        principal_year_english_percent = []
        principal_year_nonenglish_percent = []
        for index in year:
            principal_year_nonenglish_percent.append(len(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index)]) / len(df3_principal[df3_principal['CompleteYears'] == index]))
            principal_year_english_percent.append(len(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index)]) / len(df3_principal[df3_principal['CompleteYears'] == index]))    
            
        principal_year_lang_percent = np.transpose([principal_year_english_percent, principal_year_nonenglish_percent])
        principal_year_lang_percent_plot = pd.DataFrame(principal_year_lang_percent, columns=['English speaking', 'Non-english speaking'])
        plot = principal_year_lang_percent_plot.plot(kind='bar', stacked=True)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('Percentage %')
        plot.set_title('Language spoken')
        plt.savefig(IMG_DIR+'img_'+'language_spoken'+'.png', dpi=500)
        f.write("\n$img_"+"language_spoken = \""+str(WEB_HOST+"img_"+"language_spoken"+".png")+"\";")
        plt.cla()
        

        #### 1.3 Is language affecting academic result?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_academic_english = []
        principal_year_academic_nonenglish = []
        for index in year:
            principal_year_academic_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'Perc_Academic'].mean())
            principal_year_academic_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'Perc_Academic'].mean())
            
            
        principal_year_academic_language = np.transpose([principal_year_academic_english, principal_year_academic_nonenglish])
        principal_year_academic_language_plot = pd.DataFrame(principal_year_academic_language, columns=['English speaking', 'Non-english speaking'])
        plot = principal_year_academic_language_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('Academic result')
        plot.set_title('Average academic result of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_academic_result_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_academic_result_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_academic_result_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### 2 K6
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_k6 = []
        for index in year:
            principal_year_k6.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'k6_overall'].mean())
            
        plt.bar(year, principal_year_k6)
        plt.xlabel('Years completed in the school')
        plt.ylabel('K6 score')
        plt.title('Avearge K6 score of student')
        plt.savefig(IMG_DIR+'img_'+'average_k6_score_of_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_k6_score_of_student = \""+str(WEB_HOST+"img_"+"average_k6_score_of_student"+".png")+"\";")
        plt.cla()


        #### 2.1 How many 'problem' students?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_k6_problemn = []
        for index in year:
            principal_year_k6_problemn.append(df3_principal.loc[(df3_principal['CompleteYears'] == index) & (df3_principal['k6_overall'] >= 16), 'k6_overall'].count())

        plt.bar(year, principal_year_k6_problemn)
        plt.xlabel('Years completed in the school')
        plt.ylabel('No. of student')
        plt.title('Student with K6 above boderline')
        plt.savefig(IMG_DIR+'img_'+'student_with_k6_above_borderline'+'.png', dpi=500)
        f.write("\n$img_"+"student_with_k6_above_borderline = \""+str(WEB_HOST+"img_"+"student_with_k6_above_borderline"+".png")+"\";")
        plt.cla()
                
                
        #### 2.2 Who are the 'problem' students?
        principal_k6_problemn_list = df3_principal[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'House', 'k6_overall']][(df3_principal['k6_overall'] >= 16)].sort_values(by='CompleteYears')


        #### 2.3 Is language affecting K6?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_k6_english = []
        principal_year_k6_nonenglish = []
        for index in year:
            principal_year_k6_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'k6_overall'].mean())
            principal_year_k6_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'k6_overall'].mean())
            
        principal_year_k6_language = np.transpose([principal_year_k6_english, principal_year_k6_nonenglish])
        principal_year_k6_language_plot = pd.DataFrame(principal_year_k6_language, columns=['English', 'Non-English'])
        plot = principal_year_k6_language_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('K6 score')
        plot.set_title('Average K6 score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_k6_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_k6_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_k6_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()

        ### 3 Man box
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_manbox = []
        for index in year:
            principal_year_manbox.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Manbox5_overall'].mean())
            
        plt.bar(year, principal_year_manbox)
        plt.xlabel('Years completed in the school')
        plt.ylabel('Manbox score')
        plt.title('Avearge Manbox score')
        plt.savefig(IMG_DIR+'img_'+'average_manbox_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_manbox_score = \""+str(WEB_HOST+"img_"+"average_manbox_score"+".png")+"\";")
        plt.cla()


        #### 3.1 Is language affecting Manbox?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_english_manbox = []
        principal_year_nonenglish_manbox = []
        for index in year:
            principal_year_english_manbox.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'Manbox5_overall'].mean())
            principal_year_nonenglish_manbox.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'Manbox5_overall'].mean())
            
        principal_year_manbox_lang = np.transpose([principal_year_english_manbox, principal_year_nonenglish_manbox])
        principal_year_manbox_lang_plot = pd.DataFrame(principal_year_manbox_lang, columns=['English', 'Non-English'])
        plot = principal_year_manbox_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('Manbox score')
        plot.set_title('Average Manbox score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_manbox_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_manbox_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_manbox_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### 4 Masculinity measure
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_masculinity = []
        for index in year:
            principal_year_masculinity.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Masculinity_contrained'].mean())

        plt.bar(year, principal_year_masculinity)
        plt.xlabel('Years completed in the school')
        plt.ylabel('Masculinity score')
        plt.title('Avearge Masculinity box score')
        plt.savefig(IMG_DIR+'img_'+'average_masculinity_box_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_masculinity_box_score = \""+str(WEB_HOST+"img_"+"average_masculinity_box_score"+".png")+"\";")
        plt.cla()


        #### 4.1 Is language affecting Masculinity?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_masculinity_english = []
        principal_year_masculinity_nonenglish = []
        for index in year:
            principal_year_masculinity_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'Masculinity_contrained'].mean())
            principal_year_masculinity_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'Masculinity_contrained'].mean())
            
        principal_year_masculinity_lang = np.transpose([principal_year_masculinity_english, principal_year_masculinity_nonenglish])
        principal_year_masculinity_lang_plot = pd.DataFrame(principal_year_masculinity_lang, columns=['English', 'Non-English'])
        plot = principal_year_masculinity_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('Masculinity score')
        plot.set_title('Average Masculinity score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_masculinity_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_masculinity_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_masculinity_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### 5 School engagement
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_engagement = []
        for index in year:
            principal_year_engagement.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'School_support_engage6'].mean())


        plt.bar(year, principal_year_engagement)
        plt.xlabel('Years completed in the school')
        plt.ylabel('School engagement score')
        plt.title('Avearge School engagement score')
        plt.savefig(IMG_DIR+'img_'+'average_school_engagement_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_school_engagement_score = \""+str(WEB_HOST+"img_"+"average_school_engagement_score"+".png")+"\";")
        plt.cla()


        #### 5.1 Is language affecting school engagement?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_engagement_english = []
        principal_year_engagement_nonenglish = []
        for index in year:
            principal_year_engagement_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'School_support_engage6'].mean())
            principal_year_engagement_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'School_support_engage6'].mean())
            
        principal_year_engagement_lang = np.transpose([principal_year_engagement_english, principal_year_engagement_nonenglish])
        principal_year_engagement_lang_plot = pd.DataFrame(principal_year_engagement_lang, columns=['English', 'Non-English'])
        plot = principal_year_engagement_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('School engagement score')
        plot.set_title('Average school engagement score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_school_engagement_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_school_engagement_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_school_engagement_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### 6 Learning difficulties
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_growthmindset = []
        for index in year:
            principal_year_growthmindset.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'GrowthMindset'].mean())
            
        plt.bar(year, principal_year_growthmindset)
        plt.xlabel('Years completed in the school')
        plt.ylabel('Growth Mindset score')
        plt.title('Avearge Growth Mindset score')
        plt.savefig(IMG_DIR+'img_'+'average_growth_mindset_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_growth_mindset_score = \""+str(WEB_HOST+"img_"+"average_growth_mindset_score"+".png")+"\";")
        plt.cla()


        #### 6.1 Is language affecting school engagement?
        year = []
        for i in range (11):
            year.append(i)
            
        principal_year_growthmindset_english = []
        principal_year_growthmindset_nonenglish = []
        for index in year:
            principal_year_growthmindset_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'GrowthMindset'].mean())
            principal_year_growthmindset_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'GrowthMindset'].mean())

        principal_year_growthmindset_lang = np.transpose([principal_year_growthmindset_english, principal_year_growthmindset_nonenglish])
        principal_year_growthmindset_lang_plot = pd.DataFrame(principal_year_growthmindset_lang, columns=['English', 'Non-English'])
        plot = principal_year_growthmindset_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(year, rotation=0)
        plot.set_xlabel('Years completed in the school')
        plot.set_ylabel('Growth Mindset score')
        plot.set_title('Average Growth Mindset score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_growth_mindset_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_growth_mindset_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_growth_mindset_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ## View by House
        ### a. academic result and attandance
        #### a1. What is their academic result and attandance?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

        principal_house_attandance = []
        principal_house_academic = []
        for index in house:
            principal_house_attandance.append(df3_principal.loc[df3_principal['House'] == index, 'Attendance'].mean())
            principal_house_academic.append(df3_principal.loc[df3_principal['House'] == index, 'Perc_Academic'].mean())
            
        house_acad_n_att = np.transpose([principal_house_academic, np.transpose(principal_house_attandance)])
        house_acad_n_att_plot = pd.DataFrame(house_acad_n_att, columns=['Academic', 'Attandance'])

        plot = house_acad_n_att_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('Academic result / attandance')
        plot.set_title('Average academic result and attandance')
        plt.savefig(IMG_DIR+'img_'+'average_academic_result_and_attandance'+'.png', dpi=500)
        f.write("\n$img_"+"average_academic_result_and_attandance = \""+str(WEB_HOST+"img_"+"average_academic_result_and_attandance"+".png")+"\";")
        plt.cla()


        #### a2. Which language does they speak?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

        principal_house_english_percent = []
        principal_house_nonenglish_percent = []
        for index in house:
            principal_house_english_percent.append(len(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index)]) / len(df3_principal[df3_principal['House'] == index]))
            principal_house_nonenglish_percent.append(len(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index)]) / len(df3_principal[df3_principal['House'] == index]))
            
        principal_house_lang_percent = np.transpose([principal_house_english_percent, principal_house_nonenglish_percent])
        principal_house_lang_percent_plot = pd.DataFrame(principal_house_lang_percent, columns=['English speaking', 'Non-english speaking'])
        plot = principal_house_lang_percent_plot.plot(kind='bar', stacked=True)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('Percentage %')
        plot.set_title('Language spoken')
        plt.savefig(IMG_DIR+'img_'+'language_spoken'+'.png', dpi=500)
        f.write("\n$img_"+"language_spoken = \""+str(WEB_HOST+"img_"+"language_spoken"+".png")+"\";")
        plt.cla()


        #### a3. Is language affecting academic result?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_academic_english = []
        principal_house_academic_nonenglish = []
        for index in house:
            principal_house_academic_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'Perc_Academic'].mean())
            principal_house_academic_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'Perc_Academic'].mean())
            
        principal_house_academic_language = np.transpose([principal_house_academic_english, principal_house_academic_nonenglish])
        principal_house_academic_language_plot = pd.DataFrame(principal_house_academic_language, columns=['English speaking', 'Non-english speaking'])
        plot = principal_house_academic_language_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('Academic result')
        plot.set_title('Average academic result of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_academic_result_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_academic_result_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_academic_result_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### b. K6
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_k6 = []
        for index in house:
            principal_house_k6.append(df3_principal.loc[df3_principal['House'] == index, 'k6_overall'].mean())

        plt.bar(house, principal_house_k6)
        plt.xlabel('House')
        plt.ylabel('K6 score')
        plt.title('Avearge K6 score')
        plt.savefig(IMG_DIR+'img_'+'average_k6_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_k6_score = \""+str(WEB_HOST+"img_"+"average_k6_score"+".png")+"\";")
        plt.cla()


        #### b1. How many 'problem' students?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_k6_problemn = []
        for index in house:
            principal_house_k6_problemn.append(df3_principal.loc[(df3_principal['House'] == index) & (df3_principal['k6_overall'] >= 16), 'k6_overall'].count())
            
        plt.bar(house, principal_house_k6_problemn)
        plt.xlabel('House')
        plt.ylabel('No. of student')
        plt.title('Student with K6 above boderline')
        plt.savefig(IMG_DIR+'img_'+'student_with_k6_above_borderline'+'.png', dpi=500)
        f.write("\n$img_"+"student_with_k6_above_borderline = \""+str(WEB_HOST+"img_"+"student_with_k6_above_borderline"+".png")+"\";")
        plt.cla()


        #### b2. Who are the 'problem' students?
        principal_k6_problemn_list = df3_principal[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'House', 'k6_overall']][(df3_principal['k6_overall'] >= 16)].sort_values(by='CompleteYears')

        #### b3. Is language affecting K6?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_k6_english = []
        principal_house_k6_nonenglish = []
        for index in house:
            principal_house_k6_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'k6_overall'].mean())
            principal_house_k6_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'k6_overall'].mean())

        principal_house_k6_lang = np.transpose([principal_house_k6_english, principal_house_k6_nonenglish])
        principal_house_k6_lang_plot = pd.DataFrame(principal_house_k6_lang, columns=['English', 'Non-English'])
        plot = principal_house_k6_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('Year')
        plot.set_ylabel('K6 score')
        plot.set_title('Average K6 score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_k6_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_k6_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_k6_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### c. Man box
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_manbox = []
        for index in house:
            principal_house_manbox.append(df3_principal.loc[df3_principal['House'] == index, 'Manbox5_overall'].mean())

        plt.bar(house, principal_house_manbox)
        plt.xlabel('Year')
        plt.ylabel('Man box score')
        plt.title('Avearge Manbox score')
        plt.savefig(IMG_DIR+'img_'+'average_manbox_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_manbox_score = \""+str(WEB_HOST+"img_"+"average_manbox_score"+".png")+"\";")
        plt.cla()


        #### c1. Is language affecting Manbox?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

        principal_house_manbox_english = []
        principal_house_manbox_nonenglish = []
        for index in house:
            principal_house_manbox_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'Manbox5_overall'].mean())
            principal_house_manbox_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'Manbox5_overall'].mean())

        principal_house_manbox_lang = np.transpose([principal_house_manbox_english, principal_house_manbox_nonenglish])
        principal_house_manbox_lang_plot = pd.DataFrame(principal_house_manbox_lang, columns=['English', 'Non-English'])
        plot = principal_house_manbox_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('Manbox score')
        plot.set_title('Average Manbox score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_manbox_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_manbox_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_manbox_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### d. Masculinity measure
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_masculinity = []
        for index in house:
            principal_house_masculinity.append(df3_principal.loc[df3_principal['House'] == index, 'Masculinity_contrained'].mean())
            
        plt.bar(house, principal_house_masculinity)
        plt.xlabel('House')
        plt.ylabel('Masculinity score')
        plt.title('Avearge Masculinity score')
        plt.savefig(IMG_DIR+'img_'+'average_masculinity_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_masculinity_score = \""+str(WEB_HOST+"img_"+"average_masculinity_score"+".png")+"\";")
        plt.cla()


        #### d1. Is language affecting Masculinity?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_masculinity_english = []
        principal_house_masculinity_nonenglish = []
        for index in house:
            principal_house_masculinity_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'Masculinity_contrained'].mean())
            principal_house_masculinity_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'Masculinity_contrained'].mean())
            
        principal_house_masculinity_lang = np.transpose([principal_house_masculinity_english, principal_house_masculinity_nonenglish])
        principal_house_masculinity_lang_plot = pd.DataFrame(principal_house_masculinity_lang, columns=['English', 'Non-English'])
        plot = principal_house_masculinity_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('Masculinity score')
        plot.set_title('Average Masculinity score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_masculinity_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_masculinity_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_masculinity_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### e. School engagement
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

        principal_house_engagement = []
        for index in house:
            principal_house_engagement.append(df3_principal.loc[df3_principal['House'] == index, 'School_support_engage6'].mean())

        plt.bar(house, principal_house_engagement)
        plt.xlabel('House')
        plt.ylabel('School engagement score')
        plt.title('Avearge School engagement score')
        plt.savefig(IMG_DIR+'img_'+'average_school_engagement_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_school_engagement_score = \""+str(WEB_HOST+"img_"+"average_school_engagement_score"+".png")+"\";")
        plt.cla()


        #### e1. Is language affecting school engagement?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_engagement_english = []
        principal_house_engagement_nonenglish = []
        for index in house:
            principal_house_engagement_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'School_support_engage6'].mean())
            principal_house_engagement_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'School_support_engage6'].mean())
            
        principal_house_engagement_lang = np.transpose([principal_house_engagement_english, principal_house_engagement_nonenglish])
        principal_house_engagement_lang_plot = pd.DataFrame(principal_house_engagement_lang, columns=['English', 'Non-English'])
        plot = principal_house_engagement_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('school engagement score')
        plot.set_title('Average school engagement score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_school_engagement_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_school_engagement_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_school_engagement_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ### f. Learning difficulties
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_growthmindset = []
        for index in house:
            principal_house_growthmindset.append(df3_principal.loc[df3_principal['House'] == index, 'GrowthMindset'].mean())
            
        plt.bar(house, principal_house_growthmindset)
        plt.xlabel('House')
        plt.ylabel('Growth Mindset score')
        plt.title('Avearge Growth Mindset score')
        plt.savefig(IMG_DIR+'img_'+'average_growth_mindset_score'+'.png', dpi=500)
        f.write("\n$img_"+"average_growth_mindset_score = \""+str(WEB_HOST+"img_"+"average_growth_mindset_score"+".png")+"\";")
        plt.cla()


        #### f1. Is language affecting school engagement?
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
            
        principal_house_growthmindset_enghlish = []
        principal_house_growthmindset_nonenghlish = []
        for index in house:
            principal_house_growthmindset_enghlish.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'GrowthMindset'].mean())
            principal_house_growthmindset_nonenghlish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'GrowthMindset'].mean())
            
        principal_house_growthmindset_lang = np.transpose([principal_house_growthmindset_enghlish, principal_house_growthmindset_nonenghlish])
        principal_house_growthmindset_lang_plot = pd.DataFrame(principal_house_growthmindset_lang, columns=['English', 'Non-English'])
        plot = principal_house_growthmindset_lang_plot.plot(kind='bar', stacked=False)
        plot.set_xticklabels(house, rotation=0)
        plot.set_xlabel('House')
        plot.set_ylabel('Growth Mindset score')
        plot.set_title('Average Growth Mindset score of English and Non-English speaking student')
        plt.savefig(IMG_DIR+'img_'+'average_growth_mindset_score_of_english_and_non_english_speaking_student'+'.png', dpi=500)
        f.write("\n$img_"+"average_growth_mindset_score_of_english_and_non_english_speaking_student = \""+str(WEB_HOST+"img_"+"average_growth_mindset_score_of_english_and_non_english_speaking_student"+".png")+"\";")
        plt.cla()


        ## SNA adjanacy matrix by house

        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
        sna_cat = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice', 'net_5_Disrespect']
            
        house_html = house[0] # user select a house
        sna_cat_html = sna_cat[2] # user select a score to view

        principal_sna_house_cat = read_excel(xlsx, sheet_name=sna_cat_html)
        principal_sna_house_cat = principal_sna_house_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        principal_sna_house_participant = read_excel(xlsx, sheet_name='participants')
        principal_sna_house_plot = pd.merge(principal_sna_house_cat, principal_sna_house_participant, on=['Participant-ID'])
        principal_sna_house_plot = principal_sna_house_plot[['Participant-ID', 'Target', 'House']][principal_sna_house_plot['House'] == house_html]

        # Create a graph from the data
        G = nx.from_pandas_edgelist(principal_sna_house_plot, source='Participant-ID', target='Target')

        # Visualize the graph
        pos = nx.spring_layout(G)
        labels = {node: node for node in G.nodes()}

        # Create a figure and axis objects
        fig, ax = plt.subplots()

        # Draw the graph on the axis
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=100, node_color='skyblue', font_size=8, ax=ax)

        # Show the plot
        plt.savefig(IMG_DIR+'img_'+'adjanacy_matrix_by_house'+'.png', dpi=500)
        f.write("\n$img_"+"adjanacy_matrix_by_house = \""+str(WEB_HOST+"img_"+"adjanacy_matrix_by_house"+".png")+"\";")
        plt.cla()



        ## SNA adjanacy matrix by year

        year = []
        for i in range (11):
            year.append(i)

        sna_cat = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice', 'net_5_Disrespect']
            
        year_html = year[2] # user select a year
        sna_cat_html = sna_cat[2] # user select a sna network to view

        principal_sna_year_cat = read_excel(xlsx, sheet_name=sna_cat_html)
        principal_sna_year_cat = principal_sna_year_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        principal_sna_year_participant = read_excel(xlsx, sheet_name='participants')
        principal_sna_year_plot = pd.merge(principal_sna_year_cat, principal_sna_year_participant, on=['Participant-ID'])
        principal_sna_year_plot = principal_sna_year_plot[['Participant-ID', 'Target', 'House']][principal_sna_year_plot['CompleteYears'] == year_html]

        # Create a graph from the data
        G = nx.from_pandas_edgelist(principal_sna_year_plot, source='Participant-ID', target='Target')

        # Visualize the graph
        pos = nx.spring_layout(G)
        labels = {node: node for node in G.nodes()}

        # Create a figure and axis objects
        fig, ax = plt.subplots()

        # Draw the graph on the axis
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=100, node_color='skyblue', font_size=8, ax=ax)

        # Show the plot
        plt.savefig(IMG_DIR+'img_'+'adjanacy_matrix_by_year'+'.png', dpi=500)
        f.write("\n$img_"+"adjanacy_matrix_by_year = \""+str(WEB_HOST+"img_"+"adjanacy_matrix_by_year"+".png")+"\";")
        plt.cla()




        
        
        
        
        
        
        
        # Upload images and PHP files to FTP
        session = ftplib.FTP_TLS(FTP_HOST, FTP_USER, FTP_PASS)
        for filename in os.listdir(IMG_DIR):
            file = open(IMG_DIR+filename,'rb')
            session.storbinary('STOR '+ftpSurvey+filename, file)
            file.close()
             
        f.close()
        
        for filename in os.listdir(PHP_DIR):
            file = open(PHP_DIR+filename,'rb')
            session.storbinary('STOR '+ftpSurvey+filename, file)
            file.close()
        session.quit()
        # //Upload images and PHP files to FTP
        
        return "success"
    

class dashboard(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        
        df, xlsx = dataCleaning(survey)
        
        result = {}
            
        df1 = read_excel(xlsx, sheet_name='responses')
        df2 = read_excel(xlsx, sheet_name='participants')
        total = pd.merge(df1, df2, on=['Participant-ID'])
        completed = total[total['Status'].isin(['completed'])]
        in_progress = total[total['Status'].isin(['in progress'])]
        invited = total[total['Status'].isin(['invited'])]
        result['total'] = len(total)
        result['completed'] = len(completed)
        result['in_progress'] = len(in_progress)
        result['invited'] = len(invited)
        result['total'] = len(total)


        year = []
        for i in range (11):
            year.append(i)
            
        #participation_by_year
        count = []
        for index in year:
            count.append((df.loc[df['CompleteYears'] == index, 'CompleteYears'].count()).item())
        result['participation_by_year'] = {'year':year, 'count':count}
        
        #participation_by_house
        house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
        count = []
        for index in house:
            count.append((df.loc[df['House'] == index, 'House'].count()).item())
        result['participation_by_house'] = {'house':house, 'count':count}
        
        return result


class feedback(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        start = request_body["start"]
        
        df, xlsx = dataCleaning(survey)
        
        result = {}
        comments = df['YourComments']
        fake = Faker()
        for i in range(start, 10):
            result[fake.name()] = str(list(comments)[i])
        
        return result
        

def dataCleaning(survey):      
        if(survey == "1"):
            xlsx = xlsxJan
        else:
            xlsx = xlsxJuly
            
        # survey result  
        df = read_excel(xlsx, sheet_name='responses')

        # students attributes
        df2 = read_excel(xlsx, sheet_name='participants')

        # inner merge on participant ID
        df3 = pd.merge(df, df2, on=['Participant-ID'])

        # select only 'completed'
        df3 = df3[df3['Status'].isin(['completed'])]
        
        return df3, xlsx


