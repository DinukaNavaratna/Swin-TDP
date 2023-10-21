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
import json
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


class y_academic(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        
        df, xlsx = dataCleaning(survey)
        
        result = {}
        
        #### 1.1 What is their academic result and attandance?
        year = []
        for i in range (11):
            year.append(i)

        yr = {}
        for index in year:
            yr[index] = {'attendance': (df.loc[df['CompleteYears'] == index, 'Attendance'].mean()).item(), 'results': (df.loc[df['CompleteYears'] == index, 'Perc_Academic'].mean()).item()}
        
        result['academic_attendance'] = yr
        
        #### 1.2 Which language does they speak?
        year = []
        for i in range (11):
            year.append(i)

        yr = {}
        for index in year:
            yr[index] = {'non_english': (len(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index)]) / len(df[df['CompleteYears'] == index])), 'english': (len(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index)]) / len(df[df['CompleteYears'] == index]))}

        result['language'] = yr

        #### 1.3 Is language affecting academic result?
        year = []
        for i in range (11):
            year.append(i)
            
        yr = {}
        for index in year:
            yr[index] = {'non_english': (df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'Perc_Academic'].mean()), 'english': (df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'Perc_Academic'].mean())}

        result['academic_language'] = yr
        
        resultstring = json.dumps(result)
        if("NaN" in resultstring):
            resultstring = resultstring.replace("NaN", "0")
            result = json.loads(resultstring)
       
        return result


class y_k6(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            year = []
            for i in range (11):
                year.append(i)

            k6 = []
            for index in year:
                k6.append(df.loc[df['CompleteYears'] == index, 'k6_overall'].mean())
            
            result['k6'] = {"year":year, "k6":k6}
            
            #### 2.1 How many 'problem' students?
            year = []
            for i in range (11):
                year.append(i)

            k6_problem = []
            for index in year:
                k6_problem.append((df.loc[(df['CompleteYears'] == index) & (df['k6_overall'] >= 16), 'k6_overall'].count()).item())

            result['k6_problem'] = {"year":year, "k6_problem":k6_problem}
            
            #### 2.2 Who are the 'problem' students?
            k6_problem = df[['First-Name', 'Last-Name', 'CompleteYears', 'House', 'k6_overall']][(df['k6_overall'] >= 16)].sort_values(by='CompleteYears')
            k6_problem_list = k6_problem.values.tolist()
            result['k6_problem_list'] = k6_problem_list

            #### 2.3 Is language affecting K6?
            year = []
            for i in range (11):
                year.append(i)
                
            k6_english = []
            k6_nonenglish = []
            for index in year:
                k6_english.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'k6_overall'].mean())
                k6_nonenglish.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'k6_overall'].mean())

            result['k6_language'] = {"year":year, "k6_english":k6_english, "k6_nonenglish":k6_nonenglish}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class y_manbox(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            year = []
            for i in range (11):
                year.append(i)

            manbox = []
            for index in year:
                manbox.append(df.loc[df['CompleteYears'] == index, 'Manbox5_overall'].mean())
            
            result['manbox'] = {"year":year, "manbox":manbox}
            
            #### 3.1 Is language affecting Manbox?
            year = []
            for i in range (11):
                year.append(i)

            english_manbox = []
            nonenglish_manbox = []
            for index in year:
                english_manbox.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'Manbox5_overall'].mean())
                nonenglish_manbox.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'Manbox5_overall'].mean())
                
            result['language'] = {"year":year, "english":english_manbox, "nonenglish":nonenglish_manbox}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class y_masculinity(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            
            df, xlsx = dataCleaning(survey)
            
            result = {}
            
            year = []
            for i in range (11):
                year.append(i)

            masculinity = []
            for index in year:
                masculinity.append(df.loc[df['CompleteYears'] == index, 'Masculinity_contrained'].mean())
            
            result['masculinity'] = {"year":year, "masculinity":masculinity}
            
            #### 3.1 Is language affecting masculinity?
            year = []
            for i in range (11):
                year.append(i)

            english = []
            nonenglish = []
            for index in year:
                english.append(df.loc[(df['language'] == 0) & (df['CompleteYears'] == index), 'Masculinity_contrained'].mean())
                nonenglish.append(df.loc[(df['language'] == 1) & (df['CompleteYears'] == index), 'Masculinity_contrained'].mean())
                
            result['language'] = {"year":year, "english":english, "nonenglish":nonenglish}
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


