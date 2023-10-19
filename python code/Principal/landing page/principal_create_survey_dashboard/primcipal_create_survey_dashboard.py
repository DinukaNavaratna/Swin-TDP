# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:10:47 2023

@author: User Name
"""

house_html = house[0] # user select a house
survey_score_cat_html = survey_score_cat[1] # user select a score to view

principal_survey_dashboard = []
for index in year:
    principal_survey_dashboard.append(df3_principal.loc[(df3_principal['House'] == house_html) & (df3_principal['CompleteYears'] == index), survey_score_cat_html].mean())

plt.bar(year, principal_survey_dashboard)
plt.xlabel('Years completed in the school')
plt.ylabel(survey_score_cat_html)
plt.title(survey_score_cat_html + ' score of house ' + house_html)
plt.show() # need to export to frontend