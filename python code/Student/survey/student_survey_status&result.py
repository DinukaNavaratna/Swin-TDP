# show the survey stauts
print('Your survey status is', df3_student['Status'].values[0])

# print the survey result
survet_result = df3_student[['Attendance', 'Perc_Academic', 'comfortable', 'isolated', 'criticises', 'opinion', 'bullying', 'future', 'pwi_wellbeing', 
                             'k6_1', 'k6_2', 'k6_3', 'k6_4', 'k6_5', 'k6_6', 'Intelligence1', 'COVID', 'Intelligence2', 
                             'Manbox5_1', 'Manbox5_2', 'Manbox5_3', 'Manbox5_4', 'Manbox5_5', 'Soft', 'WomenDifferent', 'Nerds', 'MenBetterSTEM', 'YourComments']].transpose()

survet_result['Question'] = ['Attandance',
                             'Academic Result', 
                             'I feel comfortable at The School', 
                             'At school, I feel isolated because of my opinions', 
                             'When someone criticises The School, it feels like a personal insult', 
                             'At school, my opinion doesn’t count for much', 
                             'At this school, bullying is not tolerated at all', 
                             'I believe that what I learn at school will help me in my future', 
                             'How happy are you with your life as a whole?', 
                             'During the past 30 days, about how often did you feel nervous?', 
                             'During the past 30 days, about how often did you feel hopeless?', 
                             'During the past 30 days, about how often did you feel restless or fidgety?', 
                             'During the past 30 days, about how often did you feel so depressed that nothing could cheer you up?', 
                             'During the past 30 days, about how often did you feel that everything was an effort?', 
                             'During the past 30 days, about how often did you feel worthless?', 
                             'I have a certain amount of intelligence, and I can’t really do much to change it', 
                             'I feel worried that COVID-19 has had a big impact on my education.', 
                             'I can learn new things, but I can’t really change my basic intelligence.', 
                             'In my opinion a man shouldn\'t have to do household chores', 
                             'In my opinion men should use violence to get respect if necessary', 
                             'In my opinion a real man should have as many sexual partners as he can', 
                             'In my opinion a man who talks a lot about his worries, fears, and problems shouldn\'t really get respect', 
                             'In my opinion a gay guy is not a "real man"',
                             'Boys who don\’t play sport are "soft"', 
                             'Women and men are just naturally different in the way they think and behave', 
                             'Boys who get good marks at school are "nerds"', 
                             'Men are better than women at things like science, engineering, medicine and technology', 
                             'Your comments']

survet_result.reset_index(drop=True, inplace=True)
survet_result.rename(columns={11: 'Answer'}, inplace=True)
survet_result = survet_result[['Question', 'Answer']]

survet_result # need to export table to frontend
                            