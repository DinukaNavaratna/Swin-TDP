# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:00:36 2023

@author: User Name
"""

# average engement score by house and lang
principal_house_engagement_english = []
principal_house_engagement_nonenglish = []
for index in house:
    principal_house_engagement_english.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'School_support_engage6'].mean())
    principal_house_engagement_nonenglish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'School_support_engage6'].mean())

principal_house_engagement_lang = np.transpose([principal_house_engagement_english, principal_house_engagement_nonenglish])
principal_house_engagement_lang_plot = pd.DataFrame(principal_house_engagement_lang, columns=['English', 'Non-English'])
plot = principal_house_engagement_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('school engagement score')
plot.set_title('Average school engagement score of English and Non-English speaking student')
plt.show() # need to export to frontend