# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:02:52 2023

@author: User Name
"""

# manbox score_group by year and lang
principal_year_english_manbox = []
principal_year_nonenglish_manbox = []
for index in year:
    principal_year_english_manbox.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'Manbox5_overall'].mean())
    principal_year_nonenglish_manbox.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'Manbox5_overall'].mean())

principal_year_manbox_lang = np.transpose([principal_year_english_manbox, principal_year_nonenglish_manbox])
principal_year_manbox_lang_plot = pd.DataFrame(principal_year_manbox_lang, columns=['English', 'Non-English'])
plot = principal_year_manbox_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(year, rotation=0)
plot.set_xlabel('Year')
plot.set_ylabel('Manbox score')
plot.set_title('Average Manbox score of English and Non-English speaking student')
plt.show() # need to export to frontend