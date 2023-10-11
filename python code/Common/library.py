# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:04:15 2023

@author: User Name
"""

# neccessary library
import numpy as np
import pandas as pd
from pandas import read_excel

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


# common variables drop down/list in all dashboard

# use in making bar graph and drop down list for user to select a school year
year = []
for i in range (11):
    year.append(i)
        
# use in making bar graph and drop down list for user to select a house
house = ['Vanguard', 'Griffin', 'Phoenix', 'Falcon', 'Redwood', 'Astral']

# use as drop down list for user to select one survey cat
survey_score_cat = ['Perc_Academic', 'Manbox5_overall', 'Masculinity_contrained', 'GrowthMindset', 'k6_overall', 'School_support_engage6']

# use as drop down list for user to select one sna cat
sna_cat = ['net_0_Friends', 'net_1_Influential', 'net_2_Feedback', 'net_3_MoreTime', 'net_4_Advice', 'net_5_Disrespect']