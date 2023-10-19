# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:12:23 2023

@author: User Name
"""

# average growth mindset by year
principal_year_growthmindset = []
for index in year:
    principal_year_growthmindset.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'GrowthMindset'].mean())

plt.bar(year, principal_year_growthmindset)
plt.xlabel('Years completed in the school')
plt.ylabel('Growth Mindset score')
plt.title('Avearge Growth Mindset score')
plt.show() # need to export to frontend