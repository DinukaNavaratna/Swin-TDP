# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:25:39 2023

@author: User Name
"""

# highest learning difficult score in a class
teacher_learning_threshold = df3_teacher['GrowthMindset'].quantile(0.95) # consider to let user to set?

teacher_learning_list = df3_teacher[['Participant-ID', 'First-Name', 'Last-Name', 'GrowthMindset']][df3_teacher['GrowthMindset'] >= teacher_learning_threshold] # need to export to frontend