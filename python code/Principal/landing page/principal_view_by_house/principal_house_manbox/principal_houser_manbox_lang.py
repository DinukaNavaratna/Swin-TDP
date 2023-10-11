# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:52:06 2023

@author: User Name
"""

# average manbox score by house and lang
principal_house_manbox_english = []
principal_house_manbox_nonenglish = []
for index in house:
    principal_house_manbox_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'Manbox5_overall'].mean())
    principal_house_manbox_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'Manbox5_overall'].mean())

principal_house_manbox_lang = np.transpose([principal_house_manbox_english, principal_house_manbox_nonenglish])
principal_house_manbox_lang_plot = pd.DataFrame(principal_house_manbox_lang, columns=['English', 'Non-English'])
plot = principal_house_manbox_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('Manbox score')
plot.set_title('Average Manbox score of English and Non-English speaking student')
plt.show() # need to export to frontend