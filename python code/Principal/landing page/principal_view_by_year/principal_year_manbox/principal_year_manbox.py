# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:54:12 2023

@author: User Name
"""

# average manbox score of school year
principal_year_manbox = []
for index in year:
    principal_year_manbox.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Manbox5_overall'].mean())

plt.bar(year, principal_year_manbox)
plt.xlabel('Year')
plt.ylabel('Man box score')
plt.title('Avearge Man box score of student')
plt.show() # need to export to frontend