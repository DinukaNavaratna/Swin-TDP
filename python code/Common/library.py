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