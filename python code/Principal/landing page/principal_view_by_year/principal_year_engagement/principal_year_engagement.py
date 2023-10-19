# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:08:18 2023

@author: User Name
"""

# avarage engement score by year
principal_year_engagement = []
for index in year:
    principal_year_engagement.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'School_support_engage6'].mean())
    
plt.bar(year, principal_year_engagement)
plt.xlabel('Years completed in the school')
plt.ylabel('School engagement score')
plt.title('Avearge School engagement score')
plt.show() # need to export to frontend