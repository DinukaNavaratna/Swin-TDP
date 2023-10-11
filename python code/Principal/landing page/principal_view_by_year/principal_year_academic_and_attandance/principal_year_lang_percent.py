# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:29:33 2023

@author: User Name
"""

# proportion of language speak in different school year
principal_year_english_percent = []
principal_year_nonenglish_percent = []
for index in year:
    principal_year_nonenglish_percent.append(len(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index)]) / len(df3_principal[df3_principal['CompleteYears'] == index]))
    principal_year_english_percent.append(len(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index)]) / len(df3_principal[df3_principal['CompleteYears'] == index]))    

principal_year_lang_percent = np.transpose([principal_year_english_percent, principal_year_nonenglish_percent])
principal_year_lang_percent_plot = pd.DataFrame(principal_year_lang_percent, columns=['English speaking', 'Non-english speaking'])
plot = principal_year_lang_percent_plot.plot(kind='bar', stacked=True)
plot.set_xticklabels(year, rotation=0)
plot.set_xlabel('Year')
plot.set_ylabel('Percentage %')
plot.set_title('Composition of English and Non-english speaking student')
plt.show() # need to export to frontend