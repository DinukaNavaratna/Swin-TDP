# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:08:47 2023

@author: User Name
"""

# no of studnet participated, grouped by year 
principal_landing_no_of_student_by_year = []
for index in year:
    principal_landing_no_of_student_by_year.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'CompleteYears'].count())

plt.bar(year, principal_landing_no_of_student_by_year)
plt.xlabel('Years completed in the school')
plt.ylabel('No. of student')
plt.title('No. of student participated in the survey')
plt.show() # need to export the graph to frontend