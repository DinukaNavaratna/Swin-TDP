# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:04:39 2023

@author: User Name
"""

# sna disrespectful network of a house

# data source
teacher_sna_disrespectful = read_excel('Student Survey - July.xlsx', sheet_name= 'net_5_Disrespect')
teacher_sna_disrespectful = teacher_sna_disrespectful.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
teacher_sna_disrespectful_participant = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
teacher_sna_disrespectful_plot = pd.merge(teacher_sna_disrespectful, teacher_sna_disrespectful_participant, on=['Participant-ID'])
teacher_sna_disrespectful_plot = teacher_sna_disrespectful_plot[['Participant-ID', 'First-Name', 'Last-Name', 'Target']][teacher_sna_disrespectful_plot['House'] == hard_coded_house]


# Create a graph from the data
G = nx.from_pandas_edgelist(teacher_sna_disrespectful_plot, source='Participant-ID', target='Target')

# Visualize the graph
pos = nx.spring_layout(G)
labels = {node: node for node in G.nodes()}

# Create a figure and axis objects
fig, ax = plt.subplots()

# Draw the graph on the axis
nx.draw(G, pos, with_labels=True, labels=labels, node_size=100, node_color='skyblue', font_size=8, ax=ax)

# Show the plot
plt.show() # need to export to frontend