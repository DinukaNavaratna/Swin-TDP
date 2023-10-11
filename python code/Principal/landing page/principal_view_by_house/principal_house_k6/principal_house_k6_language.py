# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:48:53 2023

@author: User Name
"""

# k6 scrore by house and lang
principal_house_k6_english = []
principal_house_k6_nonenglish = []
for index in house:
    principal_house_k6_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'k6_overall'].mean())
    principal_house_k6_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'k6_overall'].mean())

principal_house_k6_lang = np.transpose([principal_house_k6_english, principal_house_k6_nonenglish])
principal_house_k6_lang_plot = pd.DataFrame(principal_house_k6_lang, columns=['English', 'Non-English'])
plot = principal_house_k6_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('Year')
plot.set_ylabel('K6 score')
plot.set_title('Average K6 score of English and Non-English speaking student')
plt.show() #need to export to frontend