# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:06:11 2023

@author: User Name
"""

victim = teacher_sna_disrespectful_plot[['Participant-ID', 'First-Name', 'Last-Name']]
victim = victim.drop_duplicates()

bully = teacher_sna_disrespectful_plot['Target']
bully = bully.drop_duplicates()