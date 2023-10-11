# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:14:39 2023

@author: User Name
"""

# average growth mindset score by year and lang
principal_year_growthmindset_english = []
principal_year_growthmindset_nonenglish = []
for index in year:
    principal_year_growthmindset_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'GrowthMindset'].mean())
    principal_year_growthmindset_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'GrowthMindset'].mean())

principal_year_growthmindset_lang = np.transpose([principal_year_growthmindset_english, principal_year_growthmindset_nonenglish])
principal_year_growthmindset_lang_plot = pd.DataFrame(principal_year_growthmindset_lang, columns=['English', 'Non-English'])
plot = principal_year_growthmindset_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(year, rotation=0)
plot.set_xlabel('Year')
plot.set_ylabel('Growth Mindset score')
plot.set_title('Average Growth Mindset score of English and Non-English speaking student')
plt.show() # need to export to frontend