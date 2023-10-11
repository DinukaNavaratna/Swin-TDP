# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 07:59:36 2023

@author: User Name
"""

# data source
# 1. survey result  
df_principal = read_excel('Student Survey - July.xlsx', sheet_name='responses') # need to change the path to open excel upload to web

# 2. students attributes
df2_principal = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov') # need to change the path to open excel upload to web

# 3. inner merge on participant ID
df3_principal = pd.merge(df_principal, df2_principal, on=['Participant-ID'])

# data cleaning - select only 'completed'
df3_principal = df3_principal[df3_principal['Status'].isin(['completed'])]]