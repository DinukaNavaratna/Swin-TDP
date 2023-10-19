# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:27:36 2023

@author: User Name
"""

# data source
# survey result  
df_teacher = read_excel('Student Survey - July.xlsx', sheet_name='responses')
# students attributes
df2_teacher = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
# inner merge on participant ID
temp_teacher_source = pd.merge(df_teacher, df2_teacher, on=['Participant-ID'])



# data cleaning
# hard-code a house for live demo
hard_coded_house = 'Vanguard'

# select only 'completed'
df3_teacher = temp_teacher_source[(temp_teacher_source['Status'].isin(['completed'])) & (temp_teacher_source['House'] == hard_coded_house)]


# common variables

# drop down list for teacher to select a student ID for visualization
teacher_studentID = df3_teacher['Participant-ID']

# frop down list for to select a SNA type
sna_cat = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice', 'net_5_Disrespect']