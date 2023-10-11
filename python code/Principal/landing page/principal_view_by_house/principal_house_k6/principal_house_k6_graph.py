# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:40:48 2023

@author: User Name
"""

# average k6 score by house
principal_house_k6 = []
for index in house:
    principal_house_k6.append(df3_principal.loc[df3_principal['House'] == index, 'k6_overall'].mean())

plt.bar(house, principal_house_k6)
plt.xlabel('House')
plt.ylabel('K6 score')
plt.title('Avearge K6 score of student')
plt.show() # need to export to frontend