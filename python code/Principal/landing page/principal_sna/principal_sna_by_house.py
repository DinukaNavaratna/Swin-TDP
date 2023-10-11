# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:18:24 2023

@author: User Name
"""

house_html = house[0] # user select a house from drop down list
sna_cat_html = sna_cat[2] # user select a sna cat from from drop down list

# data source
principal_sna_house_cat = read_excel('Student Survey - July.xlsx', sheet_name=sna_cat_html)
principal_sna_house_cat = principal_sna_house_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
principal_sna_house_participant = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
principal_sna_house_plot = pd.merge(principal_sna_house_cat, principal_sna_house_participant, on=['Participant-ID'])
principal_sna_house_plot = principal_sna_house_plot[['Participant-ID', 'Target', 'House']][principal_sna_house_plot['House'] == house_html]

# Create a graph from the data
G = nx.from_pandas_edgelist(principal_sna_house_plot, source='Participant-ID', target='Target')

# Visualize the graph
pos = nx.spring_layout(G)
labels = {node: node for node in G.nodes()}

# Create a figure and axis objects
fig, ax = plt.subplots()

# Draw the graph on the axis
nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='skyblue', font_size=8, ax=ax)

# Show the plot
plt.show() # need to export to fronend