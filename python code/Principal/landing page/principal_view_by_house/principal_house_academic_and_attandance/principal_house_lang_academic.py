# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:37:29 2023

@author: User Name
"""

# academic result by house and lang
principal_house_academic_english = []
principal_house_academic_nonenglish = []
for index in house:
    principal_house_academic_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'Perc_Academic'].mean())
    principal_house_academic_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'Perc_Academic'].mean())

principal_house_academic_language = np.transpose([principal_house_academic_english, principal_house_academic_nonenglish])
principal_house_academic_language_plot = pd.DataFrame(principal_house_academic_language, columns=['English speaking', 'Non-english speaking'])
plot = principal_house_academic_language_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('Academic result')
plot.set_title('Average academic result of English and Non-English speaking student')
plt.show() # need to export to frontend