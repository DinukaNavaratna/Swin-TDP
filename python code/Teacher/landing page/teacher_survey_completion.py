# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:34:45 2023

@author: User Name
"""


print('Percentage of non-completion = ', round((len(temp_teacher_source[temp_teacher_source['House'] == hard_coded_house]) - len(temp_teacher_source[(temp_teacher_source['Status'] == 'completed') & (temp_teacher_source['House'] == hard_coded_house)]))/len(temp_teacher_source) * 100, 2), '%')

teacher_house_survey_noncomplete = temp_teacher_source[['Participant-ID', 'First-Name', 'Last-Name', 'Email', 'Contact Number', 'Status']][(temp_teacher_source['Status'].isin(['in progress', 'invited'])) & (temp_teacher_source['House'] == hard_coded_house)] # need to export to frontend