student_sna_html = sna_cat_exclude_disresprect[4] # user select from frontend

student_sna_cat = read_excel('Student Survey - July.xlsx', sheet_name=student_sna_html)
student_sna_cat = student_sna_cat.rename(columns={'Source': 'Participant-ID', 'Target': 'Target'})
student_sna_cat = student_sna_cat[(student_sna_cat['Participant-ID'] != hard_coded_studentID) & (student_sna_cat['Target'] != hard_coded_studentID)]

student_sna_participant = read_excel('Student Survey - July.xlsx', sheet_name='participantsNov')
student_sna_plot = pd.merge(student_sna_cat, student_sna_participant, on=['Participant-ID'])
student_sna_plot = student_sna_plot[['Participant-ID', 'Target', 'House']][student_sna_plot['House'] == hard_coded_student_house]

student_sna_plot['Participant-ID'] = np.int64(student_sna_plot['Participant-ID'] / 2 * 3 + 5)
student_sna_plot['Target'] = np.int64(student_sna_plot['Target'] / 2 * 3 + 5)


# Create a graph from the data
G = nx.from_pandas_edgelist(student_sna_plot, source='Participant-ID', target='Target')

# Visualize the graph
pos = nx.spring_layout(G)
labels = {node: node for node in G.nodes()}

# Create a figure and axis objects
fig, ax = plt.subplots()

# Draw the graph on the axis
nx.draw(G, pos, with_labels=True, labels=labels, node_size=50, node_color='skyblue', font_size=8, ax=ax)

# Show the plot
plt.show()