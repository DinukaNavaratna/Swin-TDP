# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:23:20 2023

@author: User Name
"""

# no of studnet participated, grouped by house
principal_landing_no_of_student_by_house = []
for index in house:
    principal_landing_no_of_student_by_house.append(df3_principal.loc[df3_principal['House'] == index, 'House'].count())
    
plt.bar(house, principal_landing_no_of_student_by_house)
plt.xlabel('Years completed in the school')
plt.ylabel('No. of student')
plt.title('No. of student participated in the survey')
plt.show() # need to export the graph to frontend