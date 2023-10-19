student_sna_cat = sna_cat[5] # user select from frontend

student_sna = read_excel('Student Survey - July.xlsx', sheet_name=student_sna_cat)
student_sna.drop(student_sna[student_sna['Source'] != hard_coded_studentID].index, inplace=True)
np.savetxt(r'network_result.txt', student_sna.values, fmt='%d')
G = nx.read_edgelist("network_result.txt",create_using=nx.DiGraph())
nx.draw_networkx(G, with_labels=True)