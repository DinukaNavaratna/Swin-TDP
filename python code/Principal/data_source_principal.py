# For all except 'Club SNA' dashboard
# data source
# survey result  
df_principal_club = read_excel('Student Survey - July.xlsx', sheet_name='responses')
# students attributes
df2_principal_club = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
# club
club_jul = read_excel('Student Survey - July.xlsx', sheet_name='net_affiliation_0_SchoolActivit')
club_jan = read_excel('Student Survey - Jan.xlsx', sheet_name='net_affiliation_0_SchoolActivit')
student_club = club_jan.merge(club_jul, on='ID merge', how='outer')
student_club = student_club.drop_duplicates(subset=['Club', 'ID merge'], keep='first')
student_club = student_club.drop(['Source_x', 'Target_x', 'ID merge', 'Target_y'], axis=1)
student_club = student_club.rename(columns={'Source_y': 'Participant-ID'})

# inner merge on participant ID
df3_principal_club = pd.merge(df_principal_club, df2_principal_club, on=['Participant-ID'])
# outer merge student with clubs
df4_principal_club = student_club.merge(df3_principal_club, on='Participant-ID', how='outer')
# data cleaning
# select only 'completed'
df4_principal_club = df4_principal_club[df4_principal_club['Status'].isin(['completed'])]



# For 'Club SNA' dashboard only
# data source
# survey result  
df_principal_club = read_excel('Student Survey - July.xlsx', sheet_name='responses')
# students attributes
df2_principal_club = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
# club
club_jul = read_excel('Student Survey - July.xlsx', sheet_name='net_affiliation_0_SchoolActivit')
club_jan = read_excel('Student Survey - Jan.xlsx', sheet_name='net_affiliation_0_SchoolActivit')
student_club = club_jan.merge(club_jul, on='ID merge', how='outer')
student_club = student_club.drop_duplicates(subset=['Club', 'ID merge'], keep='first')
student_club = student_club.drop(['Source_x', 'Target_x', 'ID merge', 'Target_y'], axis=1)
student_club = student_club.rename(columns={'Source_y': 'Participant-ID'})

# inner merge on participant ID
df3_principal_club = pd.merge(df_principal_club, df2_principal_club, on=['Participant-ID'])

# outer merge student with clubs
df4_principal_club = student_club.merge(df3_principal_club, on='Participant-ID', how='outer')

# data cleaning
# select only 'completed'
df4_principal_club = df4_principal_club[df4_principal_club['Status'].isin(['completed'])]



# common variables

# list year for graph
year = []
for i in range (11):
    year.append(i)

# list house for graph and drop down list for user
house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

# drop down list for user for survey dashboard
survey_score_cat = ['Perc_Academic', 'Manbox5_overall', 'Masculinity_contrained', 'GrowthMindset', 'k6_overall', 'School_support_engage6']

# drop down list for user for SNA dashboard
sna_cat = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice', 'net_5_Disrespect']

# club list for Club SNA dashboard 
club_list = student_club['Club'].unique().tolist()