# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:02:28 2023

@author: User Name
"""

# average learning score by house
principal_house_growthmindset = []
for index in house:
    principal_house_growthmindset.append(df3_principal.loc[df3_principal['House'] == index, 'GrowthMindset'].mean())

plt.bar(house, principal_house_growthmindset)
plt.xlabel('House')
plt.ylabel('Growth Mindset score')
plt.title('Avearge Growth Mindset score')
plt.show() # need to export to frontend