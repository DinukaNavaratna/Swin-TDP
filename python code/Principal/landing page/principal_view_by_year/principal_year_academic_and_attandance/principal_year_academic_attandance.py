# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:21:05 2023

@author: User Name
"""

# student academic result and attandance grouped by year
principal_year_attandance = []
principal_year_academic = []
for index in year:
    principal_year_attandance.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Attendance'].mean()) 
    principal_year_academic.append(df3_principal.loc[df3_principal['CompleteYears'] == index, 'Perc_Academic'].mean()) 

year_acad_n_att = np.transpose([principal_year_academic, principal_year_attandance])
year_acad_n_att_plot = pd.DataFrame(year_acad_n_att, columns=['Academic', 'Attandance'])

plot = year_acad_n_att_plot.plot(kind='bar', stacked=False)
plot.set_xticklabels(year, rotation=0)
plot.set_xlabel('Years completed in the school')
plot.set_ylabel('Academic result / attandance')
plot.set_title('Average academic result and attandance')
plt.show() # need to export to frontend