# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:50:54 2023

@author: User Name
"""

# averag manbox score by house
principal_house_manbox = []
for index in house:
    principal_house_manbox.append(df3_principal.loc[df3_principal['House'] == index, 'Manbox5_overall'].mean())

plt.bar(house, principal_house_manbox)
plt.xlabel('Year')
plt.ylabel('Man box score')
plt.title('Avearge Man box score of student')
plt.show() # need to export to frontend