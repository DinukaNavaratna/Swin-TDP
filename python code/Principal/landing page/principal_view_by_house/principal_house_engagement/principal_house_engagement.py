# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:58:37 2023

@author: User Name
"""

# average engagement score by house
principal_house_engagement = []
for index in house:
    principal_house_engagement.append(df3_principal.loc[df3_principal['House'] == index, 'School_support_engage6'].mean())

plt.bar(house, principal_house_engagement)
plt.xlabel('House')
plt.ylabel('School engagement score')
plt.title('Avearge School engagement score of student')
plt.show() # need to export to frontend