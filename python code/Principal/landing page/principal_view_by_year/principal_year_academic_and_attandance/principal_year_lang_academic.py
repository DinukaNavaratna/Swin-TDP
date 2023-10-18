# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:53:09 2023

@author: User Name
"""

principal_year_academic_english = []
principal_year_academic_nonenglish = []
for index in year:
    principal_year_academic_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'Perc_Academic'].mean())
    principal_year_academic_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'Perc_Academic'].mean())    

principal_year_academic_language = np.transpose([principal_year_academic_english, principal_year_academic_nonenglish])
principal_year_academic_language_plot = pd.DataFrame(principal_year_academic_language, columns=['English speaking', 'Non-english speaking'])
plot = principal_year_academic_language_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(year, rotation=0)
plot.set_xlabel('Years completed in the school')
plot.set_ylabel('Academic result')
plot.set_title('Average academic result of English and Non-English speaking student')
plt.show() # need to export to frontend