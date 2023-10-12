# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:28:56 2023

@author: User Name
"""

# teacher sna view (limited to one house)
teacher_sna_html = sna_cat[5] # user select a score to view

# data source
teacher_sna_cat = read_excel('Student Survey - July.xlsx', sheet_name=teacher_sna_html)
teacher_sna_cat = teacher_sna_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
teacher_sna_participant = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
teacher_sna_plot = pd.merge(teacher_sna_cat, teacher_sna_participant, on=['Participant-ID'])
teacher_sna_plot = teacher_sna_plot[['Participant-ID', 'Target', 'House']][teacher_sna_plot['House'] == hard_coded_house]

# Create a graph from the data
G = nx.from_pandas_edgelist(teacher_sna_plot, source='Participant-ID', target='Target')

# Visualize the graph
pos = nx.spring_layout(G)
labels = {node: node for node in G.nodes()}

# Create a figure and axis objects
fig, ax = plt.subplots()

# Draw the graph on the axis
nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='skyblue', font_size=8, ax=ax)

# Show the plot
plt.show() # need to export to frontend