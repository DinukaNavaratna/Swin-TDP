# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:38:17 2023

@author: User Name
"""

# average k6 score of school year
principal_year_k6 = []
for index in year:
    principal_year_k6.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'k6_overall'].mean())
    
plt.bar(year, principal_year_k6)
plt.xlabel('Years completed in the school')
plt.ylabel('K6 score')
plt.title('Avearge K6 score of student')
plt.show() # need to export to frontend