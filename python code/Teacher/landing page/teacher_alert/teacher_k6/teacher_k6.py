# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:46:14 2023

@author: User Name
"""

teacher_k6_abnormal = df3_teacher[['Participant-ID', 'First-Name', 'Last-Name', 'k6_overall']][(df3_teacher['k6_overall'] >= 20)] # need to export list to frontend
teacher_k6_borderline = df3_teacher[['Participant-ID', 'First-Name', 'Last-Name', 'k6_overall']][(df3_teacher['k6_overall'] >= 16) & (df3_teacher['k6_overall'] < 20)] # need to export list to frontend