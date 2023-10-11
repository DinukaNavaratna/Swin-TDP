# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:54:00 2023

@author: User Name
"""

# average masculinity score by house
principal_house_masculinity = []
for index in house:
    principal_house_masculinity.append(df3_principal.loc[df3_principal['House'] == index, 'Masculinity_contrained'].mean())

plt.bar(house, principal_house_masculinity)
plt.xlabel('House')
plt.ylabel('Masculinity score')
plt.title('Avearge Masculinity box score of student')
plt.show() # need to export to frontend