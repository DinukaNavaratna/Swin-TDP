from flask_restful import Resource
from flask import request
import pandas as pd
from pandas import read_excel
from loguru import logger
from faker import Faker
import json


# data source
xlsxJan = pd.ExcelFile('resources/datasets/Student Survey - Jan.xlsx')
xlsxJuly = pd.ExcelFile('resources/datasets/Student Survey - July.xlsx')
xlsxJan1 = pd.ExcelFile('resources/datasets/Student Survey - Jan1.xlsx')
xlsxJuly1 = pd.ExcelFile('resources/datasets/Student Survey - July1.xlsx')
house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
year = []
for i in range (11):
    year.append(i)

        

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
        count = request_body["count"]
        
        df, xlsx = dataCleaning(survey)
        
        result = {}
        comments = df['YourComments']
        result['count'] = len(comments)
        comm = {}
        fake = Faker()
        start = (count*10)-10
        end = start+10
        if(end > len(comments)):
            end = len(comments)
        for i in range(start, end):
            comm[fake.name()] = str(list(comments)[i])
        result['comments'] = comm
        
        return result


class academic(Resource):
    def post(self, type):
        request_body = request.json
        survey = request_body["survey"]
        
        df, xlsx = dataCleaning(survey)
        
        result = {}
        
        #### 1.1 What is their academic result and attandance?
        yr = {}
        
        if(type == "y"):
            for index in year:
                yr[index] = {'attendance': (df.loc[df['CompleteYears'] == index, 'Attendance'].mean()).item(), 'results': (df.loc[df['CompleteYears'] == index, 'Perc_Academic'].mean()).item()}
        elif(type == "h"):
            for index in house:
                yr[index] = {'attendance': (df.loc[df['House'] == index, 'Attendance'].mean()).item(), 'results': (df.loc[df['House'] == index, 'Perc_Academic'].mean()).item()}
            
        result['academic_attendance'] = yr
        
        #### 1.2 Which language does they speak?
        yr = {}
        
        if(type == "y"):
            for index in year:
                yr[index] = {'non_english': (len(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index)]) / len(df[df['CompleteYears'] == index])), 'english': (len(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index)]) / len(df[df['CompleteYears'] == index]))}
        elif(type == "h"):
            for index in house:
                yr[index] = {'non_english': (len(df.loc[(df['language'] == 1) & (df['House'] == index)]) / len(df[df['House'] == index])), 'english': (len(df.loc[(df['language'] == 0) & (df['House'] == index)]) / len(df[df['House'] == index]))}
            
        result['language'] = yr

        #### 1.3 Is language affecting academic result?            
        yr = {}
        
        if(type == "y"):
            for index in year:
                yr[index] = {'non_english': (df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'Perc_Academic'].mean()), 'english': (df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'Perc_Academic'].mean())}
        elif(type == "h"):
            for index in house:
                yr[index] = {'non_english': (df.loc[(df['language'] == 1) & (df['House'] == index), 'Perc_Academic'].mean()), 'english': (df.loc[(df['language'] == 0) & (df['House'] == index), 'Perc_Academic'].mean())}
            
        result['academic_language'] = yr
        
        resultstring = json.dumps(result)
        if("NaN" in resultstring):
            resultstring = resultstring.replace("NaN", "0")
            result = json.loads(resultstring)
       
        return result


class k6(Resource):
    def post(self, type):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            k6 = []
            
            if(type == "y"):
                for index in year:
                    k6.append(df.loc[df['CompleteYears'] == index, 'k6_overall'].mean())
                result['k6'] = {"year":year, "k6":k6}
            elif(type == "h"):
                for index in house:
                    k6.append(df.loc[df['House'] == index, 'k6_overall'].mean())
                result['k6'] = {"year":house, "k6":k6}                
            
            #### 2.1 How many 'problem' students?
            k6_problem = []
            
            if(type == "y"):
                for index in year:
                    k6_problem.append((df.loc[(df['CompleteYears'] == index) & (df['k6_overall'] >= 16), 'k6_overall'].count()).item())
                result['k6_problem'] = {"year":year, "k6_problem":k6_problem}
            elif(type == "h"):
                for index in house:
                    k6_problem.append((df.loc[(df['House'] == index) & (df['k6_overall'] >= 16), 'k6_overall'].count()).item())
                result['k6_problem'] = {"year":house, "k6_problem":k6_problem}
            
            #### 2.2 Who are the 'problem' students?
            if(type == "y"):
                k6_problem = df[['First-Name', 'Last-Name', 'CompleteYears', 'House', 'k6_overall']][(df['k6_overall'] >= 16)].sort_values(by='CompleteYears')
            elif(type == "h"):
                k6_problem = df[['First-Name', 'Last-Name', 'CompleteYears', 'House', 'k6_overall']][(df['k6_overall'] >= 16)].sort_values(by='House')
                
            k6_problem_list = k6_problem.values.tolist()
            result['k6_problem_list'] = k6_problem_list

            #### 2.3 Is language affecting K6?                
            k6_english = []
            k6_nonenglish = []
            
            if(type == "y"):
                for index in year:
                    k6_english.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'k6_overall'].mean())
                    k6_nonenglish.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'k6_overall'].mean())
                result['k6_language'] = {"year":year, "k6_english":k6_english, "k6_nonenglish":k6_nonenglish}
            elif(type == "h"):
                for index in house:
                    k6_english.append(df.loc[(df['language'] == 0) & (df['House'] == index), 'k6_overall'].mean())
                    k6_nonenglish.append(df.loc[(df['language'] == 1) & (df['House'] == index), 'k6_overall'].mean())
                result['k6_language'] = {"year":house, "k6_english":k6_english, "k6_nonenglish":k6_nonenglish}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class manbox(Resource):
    def post(self, type):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            manbox = []
            
            if(type == "y"):
                for index in year:
                    manbox.append(df.loc[df['CompleteYears'] == index, 'Manbox5_overall'].mean())
                result['manbox'] = {"year":year, "manbox":manbox}
            elif(type == "h"):
                for index in house:
                    manbox.append(df.loc[df['House'] == index, 'Manbox5_overall'].mean())
                result['manbox'] = {"year":house, "manbox":manbox}
            
            #### 3.1 Is language affecting Manbox?
            english_manbox = []
            nonenglish_manbox = []
            
            if(type == "y"):
                for index in year:
                    english_manbox.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'Manbox5_overall'].mean())
                    nonenglish_manbox.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'Manbox5_overall'].mean())
                result['language'] = {"year":year, "english":english_manbox, "nonenglish":nonenglish_manbox}
            elif(type == "h"):
                for index in house:
                    english_manbox.append(df.loc[(df['language'] == 0) & (df['House'] == index), 'Manbox5_overall'].mean())
                    nonenglish_manbox.append(df.loc[(df['language'] == 1) & (df['House'] == index), 'Manbox5_overall'].mean())
                result['language'] = {"year":house, "english":english_manbox, "nonenglish":nonenglish_manbox}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class masculinity(Resource):
    def post(self, type):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            masculinity = []
            
            if(type == "y"):
                for index in year:
                    masculinity.append(df.loc[df['CompleteYears'] == index, 'Masculinity_contrained'].mean())
                result['masculinity'] = {"year":year, "masculinity":masculinity}
            elif(type == "h"):
                for index in house:
                    masculinity.append(df.loc[df['House'] == index, 'Masculinity_contrained'].mean())
                result['masculinity'] = {"year":house, "masculinity":masculinity}
            
            #### 3.1 Is language affecting masculinity?
            english = []
            nonenglish = []
            
            if(type == "y"):
                for index in year:
                    english.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'Masculinity_contrained'].mean())
                    nonenglish.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'Masculinity_contrained'].mean())
                result['language'] = {"year":year, "english":english, "nonenglish":nonenglish}
            elif(type == "h"):
                for index in house:
                    english.append(df.loc[(df['language'] == 0) & (df['House'] == index), 'Masculinity_contrained'].mean())
                    nonenglish.append(df.loc[(df['language'] == 1) & (df['House'] == index), 'Masculinity_contrained'].mean())
                result['language'] = {"year":house, "english":english, "nonenglish":nonenglish}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class engagement(Resource):
    def post(self, type):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            engagement = []
            
            if(type == "y"):
                for index in year:
                    engagement.append(df.loc[df['CompleteYears'] == index, 'School_support_engage6'].mean())
                result['engagement'] = {"year":year, "engagement":engagement}
            elif(type == "h"):
                for index in house:
                    engagement.append(df.loc[df['House'] == index, 'School_support_engage6'].mean())
                result['engagement'] = {"year":house, "engagement":engagement}
            
            #### 5.1 Is language affecting school engagement?
            english = []
            nonenglish = []
            
            if(type == "y"):
                for index in year:
                    english.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'School_support_engage6'].mean())
                    nonenglish.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'School_support_engage6'].mean())
                result['language'] = {"year":year, "english":english, "nonenglish":nonenglish}
            elif(type == "h"):
                for index in house:
                    english.append(df.loc[(df['language'] == 0) & (df['House'] == index), 'School_support_engage6'].mean())
                    nonenglish.append(df.loc[(df['language'] == 1) & (df['House'] == index), 'School_support_engage6'].mean())
                result['language'] = {"year":house, "english":english, "nonenglish":nonenglish}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class growthmindset(Resource):
    def post(self, type):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            growthmindset = []
            
            if(type == "y"):
                for index in year:
                    growthmindset.append(df.loc[df['CompleteYears'] == index, 'GrowthMindset'].mean())
                result['growthmindset'] = {"year":year, "growthmindset":growthmindset}
            elif(type == "h"):
                for index in house:
                    growthmindset.append(df.loc[df['House'] == index, 'GrowthMindset'].mean())
                result['growthmindset'] = {"year":house, "growthmindset":growthmindset}
            
            #### 5.1 Is language affecting GrowthMindset?
            english = []
            nonenglish = []
            
            if(type == "y"):
                for index in year:
                    english.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'GrowthMindset'].mean())
                    nonenglish.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'GrowthMindset'].mean())
                result['language'] = {"year":year, "english":english, "nonenglish":nonenglish}
            elif(type == "h"):
                for index in house:
                    english.append(df.loc[(df['language'] == 0) & (df['House'] == index), 'GrowthMindset'].mean())
                    nonenglish.append(df.loc[(df['language'] == 1) & (df['House'] == index), 'GrowthMindset'].mean())
                result['language'] = {"year":house, "english":english, "nonenglish":nonenglish}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class clubs(Resource):
    def post(self):
        try:
            request_body = request.json
            club = request_body["club"]
            cat = request_body["cat"]
            
            result = {}
            
            # Get the clubs
            df_principal_club = read_excel(xlsxJuly1, sheet_name='responses')
            df2_principal_club = read_excel(xlsxJuly1, sheet_name='participantsNov')
            
            club_jul = read_excel(xlsxJuly1, sheet_name='net_affiliation_0_SchoolActivit')
            club_jan = read_excel(xlsxJan1, sheet_name='net_affiliation_0_SchoolActivit')
            student_club = club_jan.merge(club_jul, on='ID merge', how='outer')
            student_club = student_club.drop_duplicates(subset=['Club', 'ID merge'], keep='first')
            student_club = student_club.drop(['Source_x', 'Target_x', 'ID merge', 'Target_y'], axis=1)
            student_club = student_club.rename(columns={'Source_y': 'Participant-ID'})
            
            df3_principal_club = pd.merge(df_principal_club, df2_principal_club, on=['Participant-ID'])
            df4_principal_club = student_club.merge(df3_principal_club, on='Participant-ID', how='outer')
            df4_principal_club = df4_principal_club[df4_principal_club['Status'].isin(['completed'])]
            
            club_list = student_club['Club'].unique().tolist()
            logger.info(club_list)
            # //Get the clubs
            
            club_html = club # user select a house
            sna_cat_html = cat # user select a score to view
            
            principal_sna_club_cat = read_excel(xlsxJuly1, sheet_name=sna_cat_html)
            principal_sna_club_cat = principal_sna_club_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
            principal_sna_club_participant = read_excel(xlsxJuly1, sheet_name='participantsNov')
            
            principal_sna_club_plot = pd.merge(principal_sna_club_cat, principal_sna_club_participant, on=['Participant-ID'])
            principal_sna_club_plot = student_club.merge(principal_sna_club_plot, on='Participant-ID', how='outer')
            principal_sna_club_plot = (principal_sna_club_plot[['Participant-ID', 'Target', 'Club']]).dropna()
            
            
            result['source'] = (principal_sna_club_plot['Participant-ID'].tolist())
            result['target'] = (principal_sna_club_plot['Target'].tolist())
            result['club'] = (principal_sna_club_plot['Club'].tolist())
            
            return result
        except Exception as ex:
            return "failed - "+str(ex)


    