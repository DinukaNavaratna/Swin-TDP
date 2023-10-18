# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:39:24 2023

@author: User Name
"""


# no. of student with >boderline score
principal_year_k6_problemn = []
for index in year:
    principal_year_k6_problemn.append(df3_principal.loc[(df3_principal['CompleteYears'] == index) & (df3_principal['k6_overall'] >= 16), 'k6_overall'].count())

plt.bar(year, principal_year_k6_problemn)
plt.xlabel('Years completed in the school')
plt.ylabel('No. of student')
plt.title('No. of student with K6 above boderline')
plt.show() # need to export to frontend