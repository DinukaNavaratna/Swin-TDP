# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:55:41 2023

@author: User Name
"""

# average masculinity score by house and lang
principal_house_masculinity_english = []
principal_house_masculinity_nonenglish = []
for index in house:
    principal_house_masculinity_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'Masculinity_contrained'].mean())
    principal_house_masculinity_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'Masculinity_contrained'].mean())

principal_house_masculinity_lang = np.transpose([principal_house_masculinity_english, principal_house_masculinity_nonenglish])
principal_house_masculinity_lang_plot = pd.DataFrame(principal_house_masculinity_lang, columns=['English', 'Non-English'])
plot = principal_house_masculinity_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('Masculinity score')
plot.set_title('Average Masculinity score of English and Non-English speaking student')
plt.show() # need to export to frontend