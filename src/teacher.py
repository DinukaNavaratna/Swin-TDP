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
houses = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
year = []
for i in range (11):
    year.append(i)

        
def dataCleaning(survey, house):
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
        if(house == ""):
            df3 = df3[df3['Status'].isin(['completed'])]
        else:
            df3 = df3[df3['Status'].isin(['completed']) & (df3['House'] == house)]
        
        return df3, xlsx


class Tdashboard(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        house = request_body["house"]
        
        df, xlsx = dataCleaning(survey, house)
        
        result = {}
            
        df1 = read_excel(xlsx, sheet_name='responses')
        df2 = read_excel(xlsx, sheet_name='participants')
        total = pd.merge(df1, df2, on=['Participant-ID'])
        completed = total[total['Status'].isin(['completed'])]
        in_progress = total[total['Status'].isin(['in progress'])]
        invited = total[total['Status'].isin(['invited'])]
        htotal = total[total['House'] == house]
        hcompleted = completed[completed['House'] == house]
        hin_progress = in_progress[in_progress['House'] == house]
        hinvited = invited[invited['House'] == house]
        result['total'] = len(total)
        result['completed'] = len(completed)
        result['invited'] = len(invited)
        result['in_progress'] = len(invited)
        result['htotal'] = len(htotal)
        result['hcompleted'] = len(hcompleted)
        result['hin_progress'] = len(hin_progress)
        result['hinvited'] = len(hinvited)
        
        hincomplete_list = (htotal[['First-Name', 'Last-Name', 'Email', 'Status']][(htotal['Status'].isin(['in progress', 'invited']))]).values.tolist()
        result['hincomplete_list'] = hincomplete_list
        
        #participation_by_house
        count = []
        for index in houses:
            count.append((completed.loc[completed['House'] == index, 'House'].count()).item())
        result['participation_by_house'] = {'house':house, 'count':count}
        
        return result


class Tfeedback(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        count = request_body["count"]
        house = request_body["house"]
        
        df, xlsx = dataCleaning(survey, house)
        
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


class Tk6(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            house = request_body["house"]
            
            df, xlsx = dataCleaning(survey, house)
            
            result = {}
            
            abnormal = df[['First-Name', 'Last-Name', 'Email', 'CompleteYears', 'House', 'k6_overall']][(df['k6_overall'] >= 20)].sort_values(by='k6_overall')
            abnormal = abnormal.values.tolist()
            result['abnormal'] = abnormal
            
            borderline = df[['First-Name', 'Last-Name', 'Email', 'CompleteYears', 'House', 'k6_overall']][(df['k6_overall'] >= 16) & (df['k6_overall'] < 20)].sort_values(by='k6_overall')
            borderline = borderline.values.tolist()
            result['borderline'] = borderline

            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class Tdisrespect(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            house = request_body["house"]
            
            df, xlsx = dataCleaning(survey, house)
            
            result = {}
            
            disrespectful = read_excel(xlsx, sheet_name= 'net_5_Disrespect')
            disrespectful = disrespectful.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
            disrespectful_participant = read_excel(xlsx, sheet_name='participants')
            disrespectful_plot = pd.merge(disrespectful, disrespectful_participant, on=['Participant-ID'])
            disrespectful_plot = disrespectful_plot[['Participant-ID', 'First-Name', 'Last-Name', 'Target']][disrespectful_plot['House'] == house]
            result['disrespectee'] = disrespectful_plot.values.tolist()
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)



