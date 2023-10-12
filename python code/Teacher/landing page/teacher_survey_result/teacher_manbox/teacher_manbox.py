# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:13:57 2023

@author: User Name
"""

# top (x%) man box score in a house



teacher_man_box_threshold = df3_teacher['Manbox5_overall'].quantile(0.90) # consider to allow user to set?

teacher_manbox_list = df3_teacher[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'Manbox5_overall']][df3_teacher['Manbox5_overall'] >= teacher_man_box_threshold] # need to export to frontend