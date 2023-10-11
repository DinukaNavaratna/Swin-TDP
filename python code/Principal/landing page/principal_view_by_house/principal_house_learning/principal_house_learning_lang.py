# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:05:29 2023

@author: User Name
"""

# average learning score by house and lang
principal_house_growthmindset_enghlish = []
principal_house_growthmindset_nonenghlish = []
for index in house:
    principal_house_growthmindset_enghlish.append(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index), 'GrowthMindset'].mean())
    principal_house_growthmindset_nonenghlish.append(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index), 'GrowthMindset'].mean())

principal_house_growthmindset_lang = np.transpose([principal_house_growthmindset_enghlish, principal_house_growthmindset_nonenghlish])
principal_house_growthmindset_lang_plot = pd.DataFrame(principal_house_growthmindset_lang, columns=['English', 'Non-English'])
plot = principal_house_growthmindset_lang_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('Growth Mindset score')
plot.set_title('Average Growth Mindset score of English and Non-English speaking student')
plt.show() # need to export to frontend