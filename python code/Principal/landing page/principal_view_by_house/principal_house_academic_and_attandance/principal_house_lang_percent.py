# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:35:34 2023

@author: User Name
"""

# proportion of language speak in different school year
principal_house_english_percent = []
principal_house_nonenglish_percent = []
for index in house:
    principal_house_english_percent.append(len(df3_principal.loc[(df3_principal['language'] == 1) & (df3_principal['House'] == index)]) / len(df3_principal[df3_principal['House'] == index]))
    principal_house_nonenglish_percent.append(len(df3_principal.loc[(df3_principal['language'] == 0) & (df3_principal['House'] == index)]) / len(df3_principal[df3_principal['House'] == index]))    

principal_house_lang_percent = np.transpose([principal_house_english_percent, principal_house_nonenglish_percent])
principal_house_lang_percent_plot = pd.DataFrame(principal_house_lang_percent, columns=['English speaking', 'Non-english speaking'])
plot = principal_house_lang_percent_plot.plot(kind='bar', stacked=True)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('Percentage %')
plot.set_title('Composition of Engliah and Non-english speaking student')
plt.show() #need to export to frontend