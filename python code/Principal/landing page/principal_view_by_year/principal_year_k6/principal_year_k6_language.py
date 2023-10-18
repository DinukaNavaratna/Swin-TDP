# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:43:17 2023

@author: User Name
"""

# k6 score with language view (year)
principal_year_k6_english = []
principal_year_k6_nonenglish = []
for index in year:
    principal_year_k6_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['CompleteYears'] == index), 'k6_overall'].mean())
    principal_year_k6_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['CompleteYears'] == index), 'k6_overall'].mean())

principal_year_k6_language = np.transpose([principal_year_k6_english, principal_year_k6_nonenglish])
principal_year_k6_language_plot = pd.DataFrame(principal_year_k6_language, columns=['English', 'Non-English'])
plot = principal_year_k6_language_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(year, rotation=0)
plot.set_xlabel('Years completed in the school')
plot.set_ylabel('K6 score')
plot.set_title('Average K6 score of English and Non-English speaking student')   
plt.show() # need to export to frontend