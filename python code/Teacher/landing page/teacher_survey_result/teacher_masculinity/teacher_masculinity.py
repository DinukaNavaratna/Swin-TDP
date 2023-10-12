# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:17:11 2023

@author: User Name
"""

# top masculinity score in a house
teacher_masculinity_threshold = df3_teacher['Masculinity_contrained'].quantile(0.95) # consider to allow user to set?

teacher_masculinity_list = df3_teacher[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'Masculinity_contrained']][df3_teacher['Masculinity_contrained'] >= teacher_masculinity_threshold] # need to export to frontend