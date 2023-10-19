# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:43:52 2023

@author: User Name
"""

# kb score > boderline by house
principal_house_k6_problemn = []
for index in house:
    principal_house_k6_problemn.append(df3_principal.loc[(df3_principal['House'] == index) & (df3_principal['k6_overall'] >= 16), 'k6_overall'].count())

plt.bar(house, principal_house_k6_problemn)
plt.xlabel('House')
plt.ylabel('No. of student')
plt.title('Student with K6 above boderline')
plt.show() # need to export to frontend