import pandas as pd
import networkx as nx
import warnings
import matplotlib.pyplot as plt
import numpy as np

xlsx = pd.ExcelFile('sample.xlsx')
df = pd.read_excel(xlsx, sheet_name='net_0_Friends')
par = pd.read_excel(xlsx, sheet_name='participants')

attn_dict = par.set_index('Participant-ID')['Attendance'].to_dict()
aca_dict = par.set_index('Participant-ID')['Perc_Academic'].to_dict()

df.head()

us_graph = nx.from_pandas_edgelist(df,source="Source",target="Target")


degree_centrality = nx.degree(us_graph)

a = 0
c = 0
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []

degree_centrality = sorted(degree_centrality, key=lambda x: x[1], reverse=False)

for key, value in degree_centrality:
    a = a+1
    if key in attn_dict:
        c=c+1
        y.append(value)
        y1.append((attn_dict[key]/10))
        y2.append((aca_dict[key]/10))
        x.append(c)
        x1.append(c)
        x2.append(c)
        print(str(key) + " - " + str(value) + " - " + str(attn_dict[key]) + " - " + str(aca_dict[key]))
    #if c == 10:
    #    break

print(a)
print(c)
  
plt.plot(x, y, label="Friends")
plt.plot(x1, y1, '-.', label="Attendance")
plt.legend(loc="upper right")
plt.xlabel("Students") 
plt.ylabel("Friends/Attendance")
plt.xticks([])
plt.yticks([])
plt.title("Friends/Attendance") 
plt.show()
plt.savefig('Friends_Attendance.png', dpi=500)

plt.cla()
  
plt.plot(x, y, label="Friends")
plt.plot(x2, y2, '-.', label="Performance")
plt.legend(loc="upper right")
plt.xlabel("Students") 
plt.ylabel("Friends/Performance")
plt.xticks([])
plt.yticks([])
plt.title("Friends/Performance") 
plt.show()
plt.savefig('Friends_Performance.png', dpi=500)

plt.cla()

