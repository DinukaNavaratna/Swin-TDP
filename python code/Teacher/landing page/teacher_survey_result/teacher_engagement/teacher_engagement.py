# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:22:34 2023

@author: User Name
"""

# highest engagement score in a house
teacher_engagment_threshold = df3_teacher['School_support_engage6'].quantile(0.95)# consider to let user to set

teacher_engagment_threshold_list = df3_teacher[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears' , 'School_support_engage6']][df3_teacher['School_support_engage6'] >= teacher_engagment_threshold] # need to export to frontend