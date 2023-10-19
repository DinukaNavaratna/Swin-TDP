club_html = club_list[3] # user select a house from frontend
sna_cat_html = sna_cat[5] # user select a score from frontend

principal_sna_club_cat = read_excel('Student Survey - July.xlsx', sheet_name=sna_cat_html)
principal_sna_club_cat = principal_sna_club_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
principal_sna_club_participant = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')


principal_sna_club_plot = pd.merge(principal_sna_club_cat, principal_sna_club_participant, on=['Participant-ID'])
principal_sna_club_plot = student_club.merge(principal_sna_club_plot, on='Participant-ID', how='outer')
principal_sna_club_plot = principal_sna_club_plot[['Participant-ID', 'Target', 'Club']][principal_sna_club_plot['Club'] == club_html]

# Create a graph from the data
G = nx.from_pandas_edgelist(principal_sna_club_plot, source='Participant-ID', target='Target')

# Visualize the graph
pos = nx.spring_layout(G)
labels = {node: node for node in G.nodes()}

# Create a figure and axis objects
fig, ax = plt.subplots()

# Draw the graph on the axis
nx.draw(G, pos, with_labels=True, labels=labels, node_size=100, node_color='skyblue', font_size=8, ax=ax)

# Show the plot
plt.show()