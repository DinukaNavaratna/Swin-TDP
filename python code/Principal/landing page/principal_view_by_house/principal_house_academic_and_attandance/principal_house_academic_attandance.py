# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:33:49 2023

@author: User Name
"""

# average academic and attandance by house
principal_house_attandance = []
principal_house_academic = []
for index in house:
    principal_house_attandance.append(df3_principal.loc[df3_principal['House'] == index, 'Attendance'].mean())
    principal_house_academic.append(df3_principal.loc[df3_principal['House'] == index, 'Perc_Academic'].mean())

house_acad_n_att = np.transpose([principal_house_academic, np.transpose(principal_house_attandance)])
house_acad_n_att_plot = pd.DataFrame(house_acad_n_att, columns=['Academic', 'Attandance'])

plot = house_acad_n_att_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(house, rotation=0)
plot.set_xlabel('House')
plot.set_ylabel('Academic result / attandance')
plot.set_title('Average academic result and attandance of student of each house')
plt.show() # need to export to frontend