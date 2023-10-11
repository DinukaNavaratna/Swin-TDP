# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:42:05 2023

@author: User Name
"""


# list of name with >boderline 
principal_year_k6_problemn_list = df3_principal[['Participant-ID', 'First-Name', 'Last-Name', 'CompleteYears', 'House', 'k6_overall']][(df3_principal['k6_overall'] >= 16)].sort_values(by='CompleteYears')