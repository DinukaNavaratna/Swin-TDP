# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:50:25 2023

@author: User Name
"""

teacher_sna_cat = sna_cat[2] # user select one sna network from drop down list
teacher_studentID_html = teacher_studentID.iloc[1] # user select a student from drop down list

teacher_sna_student = read_excel('Student Survey - July.xlsx', sheet_name=teacher_sna_cat)
teacher_sna_student.drop(teacher_sna_student[teacher_sna_student['Source'] != teacher_studentID_html].index, inplace=True)
np.savetxt(r'network_result.txt', teacher_sna_student.values, fmt='%d')
G = nx.read_edgelist("network_result.txt",create_using=nx.DiGraph())
nx.draw_networkx(G, with_labels=True) # need to export to frontend