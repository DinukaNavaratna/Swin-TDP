# data source
# survey result  
df_student = read_excel('Student Survey - July.xlsx', sheet_name='responses')
# students attributes
df2_student = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
# inner merge on participant ID
temp_student_source = pd.merge(df_student, df2_student, on=['Participant-ID'])

# data cleaning
# hard-code a house
hard_coded_studentID = 37915
hard_coded_student_house = 'Griffin'

# filter to show only the student
df3_student = temp_student_source[temp_student_source['Participant-ID'] == hard_coded_studentID]

# common variable
# drop down list for user toe select a SNA type
sna_cat = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice', 'net_5_Disrespect']
# drop down list exclude disrespect, to protact sensitive information 
sna_cat_exclude_disresprect = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice']