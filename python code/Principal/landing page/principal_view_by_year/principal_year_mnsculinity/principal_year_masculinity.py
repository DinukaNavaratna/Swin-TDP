# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:03:48 2023

@author: User Name
"""

# average masculinity score by year
principal_year_masculinity = []
for index in year:
    principal_year_masculinity.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Masculinity_contrained'].mean())

plt.bar(year, principal_year_masculinity)
plt.xlabel('Years completed in the school')
plt.ylabel('Masculinity score')
plt.title('Avearge Masculinity box score of student')
plt.show() # need to export to frontend