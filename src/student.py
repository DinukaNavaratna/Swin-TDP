from flask_restful import Resource
from flask import request
import pandas as pd
from pandas import read_excel
from loguru import logger
from faker import Faker
import json
import numpy as np


# data source
xlsxJan = pd.ExcelFile('resources/datasets/Student Survey - Jan.xlsx')
xlsxJuly = pd.ExcelFile('resources/datasets/Student Survey - July.xlsx')
houses = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']
year = []
for i in range (11):
    year.append(i)


class Sdashboard(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        house = request_body["house"]
        sid = np.int64(request_body["sid"])
        
        xlsx = xlsxJuly
        
        result = {}
            
        df1 = read_excel(xlsx, sheet_name='responses')
        df2 = read_excel(xlsx, sheet_name='participants')
        src = pd.merge(df1, df2, on=['Participant-ID'])
        
        student = src[src['Participant-ID'] == sid]
        result['status'] = (student['Status'].values[0])
        
        survey_result = student[['Attendance', 'Perc_Academic', 'comfortable', 'isolated', 'criticises', 'opinion', 'bullying', 'future', 'pwi_wellbeing', 'k6_1', 'k6_2', 'k6_3', 'k6_4', 'k6_5', 'k6_6', 'Intelligence1', 'COVID', 'Intelligence2', 'Manbox5_1', 'Manbox5_2', 'Manbox5_3', 'Manbox5_4', 'Manbox5_5', 'Soft', 'WomenDifferent', 'Nerds', 'MenBetterSTEM', 'YourComments']].transpose()
        survey_result['Question'] = ['Attandance',
                             'Academic Result', 
                             'I feel comfortable at The School', 
                             'At school, I feel isolated because of my opinions', 
                             'When someone criticises The School, it feels like a personal insult', 
                             'At school, my opinion doesn\'t count for much', 
                             'At this school, bullying is not tolerated at all', 
                             'I believe that what I learn at school will help me in my future', 
                             'How happy are you with your life as a whole?', 
                             'During the past 30 days, about how often did you feel nervous?', 
                             'During the past 30 days, about how often did you feel hopeless?', 
                             'During the past 30 days, about how often did you feel restless or fidgety?', 
                             'During the past 30 days, about how often did you feel so depressed that nothing could cheer you up?', 
                             'During the past 30 days, about how often did you feel that everything was an effort?', 
                             'During the past 30 days, about how often did you feel worthless?', 
                             'I have a certain amount of intelligence, and I can\'t really do much to change it', 
                             'I feel worried that COVID-19 has had a big impact on my education.', 
                             'I can learn new things, but I can\'t really change my basic intelligence.', 
                             'In my opinion a man shouldn\'t have to do household chores', 
                             'In my opinion men should use violence to get respect if necessary', 
                             'In my opinion a real man should have as many sexual partners as he can', 
                             'In my opinion a man who talks a lot about his worries, fears, and problems shouldn\'t really get respect', 
                             'In my opinion a gay guy is not a "real man"',
                             'Boys who don\'t play sport are "soft"', 
                             'Women and men are just naturally different in the way they think and behave', 
                             'Boys who get good marks at school are "nerds"', 
                             'Men are better than women at things like science, engineering, medicine and technology', 
                             'Your comments']
        
        survey_result.reset_index(drop=True, inplace=True)
        survey_result.rename(columns={11: 'Answer'}, inplace=True)
        survey_result = survey_result[['Question', 'Answer']]
        
        result['questions'] = (survey_result['Question'].values.tolist())
        result['answers'] = (survey_result['Answer'].values.tolist())
        
        
        return result


class Snominations(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        house = request_body["house"]
        sid = np.int64(request_body["sid"])
        
        xlsx = xlsxJuly
        
        result = {}

        student_sna = read_excel(xlsx, sheet_name='net_0_Friends')
        student_sna.drop(student_sna[student_sna['Source'] != sid].index, inplace=True)
        result['net_0_Friends'] = (student_sna.values).tolist()

        student_sna = read_excel(xlsx, sheet_name='net_1_Influential')
        student_sna.drop(student_sna[student_sna['Source'] != sid].index, inplace=True)
        result['net_1_Influential'] = (student_sna.values).tolist()

        student_sna = read_excel(xlsx, sheet_name='net_2_Feedback')
        student_sna.drop(student_sna[student_sna['Source'] != sid].index, inplace=True)
        result['net_2_Feedback'] = (student_sna.values).tolist()

        student_sna = read_excel(xlsx, sheet_name='net_3_MoreTime')
        student_sna.drop(student_sna[student_sna['Source'] != sid].index, inplace=True)
        result['net_3_MoreTime'] = (student_sna.values).tolist()

        student_sna = read_excel(xlsx, sheet_name='net_4_Advice')
        student_sna.drop(student_sna[student_sna['Source'] != sid].index, inplace=True)
        result['net_4_Advice'] = (student_sna.values).tolist()

        student_sna = read_excel(xlsx, sheet_name='net_5_Disrespect')
        student_sna.drop(student_sna[student_sna['Source'] != sid].index, inplace=True)
        result['net_5_Disrespect'] = (student_sna.values).tolist()
        
        return result


class Scolleague(Resource):
    def post(self):
        request_body = request.json
        survey = request_body["survey"]
        house = request_body["house"]
        sid = np.int64(request_body["sid"])
        
        xlsx = xlsxJuly
        
        result = {}

        student_sna = read_excel(xlsx, sheet_name='net_0_Friends')
        student_sna = student_sna.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        student_sna = student_sna[(student_sna['Participant-ID'] != sid) & (student_sna['Target'] != sid)]
        
        student_sna_participant = read_excel(xlsx, sheet_name='participants')
        student_sna_plot = pd.merge(student_sna, student_sna_participant, on=['Participant-ID'])
        student_sna_plot = student_sna_plot[['Participant-ID', 'Target']][student_sna_plot['House'] == house]
        
        student_sna_plot['Participant-ID'] = np.int64(student_sna_plot['Participant-ID'] / 2 * 3 + 5)
        student_sna_plot['Target'] = np.int64(student_sna_plot['Target'] / 2 * 3 + 5)
        
        lis = (student_sna_plot.values).tolist()
        for i in range(len(lis)):
            lis[i][0] = maskID(lis[i][0])
            lis[i][1] = maskID(lis[i][1])
        result['net_0_Friends'] = lis
        

        student_sna = read_excel(xlsx, sheet_name='net_1_Influential')
        student_sna = student_sna.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        student_sna = student_sna[(student_sna['Participant-ID'] != sid) & (student_sna['Target'] != sid)]
        
        student_sna_participant = read_excel(xlsx, sheet_name='participants')
        student_sna_plot = pd.merge(student_sna, student_sna_participant, on=['Participant-ID'])
        student_sna_plot = student_sna_plot[['Participant-ID', 'Target']][student_sna_plot['House'] == house]
        
        student_sna_plot['Participant-ID'] = np.int64(student_sna_plot['Participant-ID'] / 2 * 3 + 5)
        student_sna_plot['Target'] = np.int64(student_sna_plot['Target'] / 2 * 3 + 5)

        lis = (student_sna_plot.values).tolist()
        for i in range(len(lis)):
            lis[i][0] = maskID(lis[i][0])
            lis[i][1] = maskID(lis[i][1])
        result['net_1_Influential'] = lis
        

        student_sna = read_excel(xlsx, sheet_name='net_2_Feedback')
        student_sna = student_sna.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        student_sna = student_sna[(student_sna['Participant-ID'] != sid) & (student_sna['Target'] != sid)]
        
        student_sna_participant = read_excel(xlsx, sheet_name='participants')
        student_sna_plot = pd.merge(student_sna, student_sna_participant, on=['Participant-ID'])
        student_sna_plot = student_sna_plot[['Participant-ID', 'Target']][student_sna_plot['House'] == house]
        
        student_sna_plot['Participant-ID'] = np.int64(student_sna_plot['Participant-ID'] / 2 * 3 + 5)
        student_sna_plot['Target'] = np.int64(student_sna_plot['Target'] / 2 * 3 + 5)

        lis = (student_sna_plot.values).tolist()
        for i in range(len(lis)):
            lis[i][0] = maskID(lis[i][0])
            lis[i][1] = maskID(lis[i][1])
        result['net_2_Feedback'] = lis
        

        student_sna = read_excel(xlsx, sheet_name='net_3_MoreTime')
        student_sna = student_sna.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        student_sna = student_sna[(student_sna['Participant-ID'] != sid) & (student_sna['Target'] != sid)]
        
        student_sna_participant = read_excel(xlsx, sheet_name='participants')
        student_sna_plot = pd.merge(student_sna, student_sna_participant, on=['Participant-ID'])
        student_sna_plot = student_sna_plot[['Participant-ID', 'Target']][student_sna_plot['House'] == house]
        
        student_sna_plot['Participant-ID'] = np.int64(student_sna_plot['Participant-ID'] / 2 * 3 + 5)
        student_sna_plot['Target'] = np.int64(student_sna_plot['Target'] / 2 * 3 + 5)

        lis = (student_sna_plot.values).tolist()
        for i in range(len(lis)):
            lis[i][0] = maskID(lis[i][0])
            lis[i][1] = maskID(lis[i][1])
        result['net_3_MoreTime'] = lis
        

        student_sna = read_excel(xlsx, sheet_name='net_4_Advice')
        student_sna = student_sna.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
        student_sna = student_sna[(student_sna['Participant-ID'] != sid) & (student_sna['Target'] != sid)]
        
        student_sna_participant = read_excel(xlsx, sheet_name='participants')
        student_sna_plot = pd.merge(student_sna, student_sna_participant, on=['Participant-ID'])
        student_sna_plot = student_sna_plot[['Participant-ID', 'Target']][student_sna_plot['House'] == house]
        
        student_sna_plot['Participant-ID'] = np.int64(student_sna_plot['Participant-ID'] / 2 * 3 + 5)
        student_sna_plot['Target'] = np.int64(student_sna_plot['Target'] / 2 * 3 + 5)

        lis = (student_sna_plot.values).tolist()
        for i in range(len(lis)):
            lis[i][0] = maskID(lis[i][0])
            lis[i][1] = maskID(lis[i][1])
        result['net_4_Advice'] = lis
        
        return result


def maskID(id):
    alp = ["A", "C", "G", "E", "W", "H", "L", "P", "M", "S"]
    id = [int(x) for x in str(id)]
    for i in range(len(id)):
        id[i] = alp[id[i]]
    return ''.join(id)