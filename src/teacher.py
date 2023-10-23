from flask_restful import Resource
from flask import request
import pandas as pd
from pandas import read_excel
from loguru import logger
from faker import Faker
import json
import numpy as np
import sys, os


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
        result['participation_by_house'] = {'house':houses, 'count':count}
        
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
            
            abnormal = df[['First-Name', 'Last-Name', 'Email', 'CompleteYears', 'House', 'k6_overall', 'Participant-ID']][(df['k6_overall'] >= 20)].sort_values(by='k6_overall')
            abnormal = abnormal.values.tolist()
            result['abnormal'] = abnormal
            
            borderline = df[['First-Name', 'Last-Name', 'Email', 'CompleteYears', 'House', 'k6_overall', 'Participant-ID']][(df['k6_overall'] >= 16) & (df['k6_overall'] < 20)].sort_values(by='k6_overall')
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
            disrespectful_participant1 = read_excel(xlsx, sheet_name='participants')
            disrespectful_participant1 = disrespectful_participant1.rename(columns={'Participant-ID': 'Target', 'First-Name': 'FirstName', 'Last-Name': 'LastName', 'House': 'Ignore'})
            disrespectful_plot = pd.merge(disrespectful, disrespectful_participant, on=['Participant-ID'])
            disrespectful_plot = pd.merge(disrespectful_plot, disrespectful_participant1, on=['Target'])
            disrespectful_plot = disrespectful_plot[['Participant-ID', 'First-Name', 'Last-Name', 'Target', 'FirstName', 'LastName']][disrespectful_plot['House'] == house]
            result['disrespect'] = disrespectful_plot.values.tolist()
            
            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class Tmanbox(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            house = request_body["house"]
            
            df, xlsx = dataCleaning(survey, house)
            
            result = {}
            
            threshold = df['Manbox5_overall'].quantile(0.95)
            manbox = df[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'Manbox5_overall']][df['Manbox5_overall'] >= threshold]
            manbox = manbox.values.tolist()
            result['manbox'] = manbox

            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class Tmasculinity(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            house = request_body["house"]
            
            df, xlsx = dataCleaning(survey, house)
            
            result = {}
            
            threshold = df['Masculinity_contrained'].quantile(0.95)
            masculinity = df[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'Masculinity_contrained']][df['Masculinity_contrained'] >= threshold]
            masculinity = masculinity.values.tolist()
            result['masculinity'] = masculinity

            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class Tengagement(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            house = request_body["house"]
            
            df, xlsx = dataCleaning(survey, house)
            
            result = {}
            
            threshold = df['School_support_engage6'].quantile(0.95)
            engagement = df[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'School_support_engage6']][df['School_support_engage6'] >= threshold]
            engagement = engagement.values.tolist()
            result['engagement'] = engagement

            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class Tgrowthmindset(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            house = request_body["house"]
            
            df, xlsx = dataCleaning(survey, house)
            
            result = {}
            
            threshold = df['GrowthMindset'].quantile(0.95)
            growthmindset = df[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'GrowthMindset']][df['GrowthMindset'] >= threshold]
            growthmindset = growthmindset.values.tolist()
            result['growthmindset'] = growthmindset

            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            return result
        except Exception as ex:
            return "failed - "+str(ex)


class Tstudent(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            category = request_body["category"]
            sid = np.int64(request_body["sid"])
            
            df, xlsx = dataCleaning(survey, "")
            
            result = {}
            
            sna_student = read_excel(xlsx, sheet_name=str(category))
            sna_student.drop(sna_student[(sna_student['Source'] != sid) & (sna_student['Target'] != sid)].index, inplace=True)
        
            result['network'] = (sna_student.values).tolist()

            resultstring = json.dumps(result)
            if("NaN" in resultstring):
                resultstring = resultstring.replace("NaN", "0")
                result = json.loads(resultstring)
        
            sur = read_excel(xlsx, sheet_name='participants')
            email = sur.loc[sur['Participant-ID'] == sid, 'Email']
            
            if email.count() != 0:
                try:
                    email = email.item()
                    sur1 = read_excel(xlsxJan, sheet_name='participants')
                    sur2 = read_excel(xlsxJuly, sheet_name='participants')
                    
                    eff1 = sur1.loc[sur1['Email'] == email, 'Perc_Effort'].item()
                    attn1 = sur1.loc[sur1['Email'] == email, 'Attendance'].item()
                    aca1 = sur1.loc[sur1['Email'] == email, 'Perc_Academic'].item()
                    
                    eff2 = sur2.loc[sur2['Email'] == email, 'Perc_Effort'].item()
                    attn2 = sur2.loc[sur2['Email'] == email, 'Attendance'].item()
                    aca2 = sur2.loc[sur2['Email'] == email, 'Perc_Academic'].item()
                
                    result['data'] = {"email":email, "eff1":eff1, "attn1":attn1, "aca1":aca1, "eff2":eff2, "attn2":attn2, "aca2":aca2}
                except:
                    result['data'] = {"email":"error"}
            else:
                result['data'] = {"email":"", "eff1":0, "attn1":0, "aca1":0, "eff2":0, "attn2":0, "aca2":0}
            
            return result
        except Exception as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return "failed (" + str(exc_tb.tb_lineno) + ") - "+str(ex)


class Tdata(Resource):
    def post(self):
        try:
            request_body = request.json
            survey = request_body["survey"]
            sid = np.int64(request_body["sid"])
            
            df, xlsx = dataCleaning(survey, "")        
        
            sur = read_excel(xlsx, sheet_name='participants')
            email = sur.loc[sur['Participant-ID'] == sid, 'Email'].item()
            
            sur1 = read_excel(xlsxJan, sheet_name='participants')
            sur2 = read_excel(xlsxJuly, sheet_name='participants')
            
            try:
                eff1 = sur1.loc[sur1['Email'] == email, 'Perc_Effort'].item()
                attn1 = sur1.loc[sur1['Email'] == email, 'Attendance'].item()
                aca1 = sur1.loc[sur1['Email'] == email, 'Perc_Academic'].item()
                
                eff2 = sur2.loc[sur2['Email'] == email, 'Perc_Effort'].item()
                attn2 = sur2.loc[sur2['Email'] == email, 'Attendance'].item()
                aca2 = sur2.loc[sur2['Email'] == email, 'Perc_Academic'].item()
                
                result = {"email":email, "eff1":eff1, "attn1":attn1, "aca1":aca1, "eff2":eff2, "attn2":attn2, "aca2":aca2}
            except:
                result = {"email":"error"}
            
            
            return result
        except Exception as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return "failed (" + str(exc_tb.tb_lineno) + ") - "+str(ex)


class Tadjanency(Resource):
    def post(self):
        try:
            request_body = request.json
            cat = request_body["cat"]
            house = request_body["house"]
            
            result = {}
            
            teacher_sna_cat = read_excel(xlsxJuly, sheet_name=cat)
            teacher_sna_cat = teacher_sna_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
            teacher_sna_participant = read_excel(xlsxJuly, sheet_name='participants')
            teacher_sna_plot = pd.merge(teacher_sna_cat, teacher_sna_participant, on=['Participant-ID'])
            teacher_sna_plot = teacher_sna_plot[['Participant-ID', 'Target', 'CompleteYears']][teacher_sna_plot['House'] == house]          
            
            result['source'] = (teacher_sna_plot['Participant-ID'].tolist())
            result['target'] = (teacher_sna_plot['Target'].tolist())
            result['club'] = (teacher_sna_plot['CompleteYears'].tolist())
            
            return result
        except Exception as ex:
            return "failed - "+str(ex)





