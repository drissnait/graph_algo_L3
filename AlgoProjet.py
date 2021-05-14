# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:44:53 2020

@author: driss
"""

import pandas as pd
import csv
import re   
import networkx as nx
import os
from networkx.drawing.nx_agraph import write_dot
import matplotlib.pyplot as plt
from graphviz import Digraph

print("okok")
fileActeurs = "IMDB-Movie-Data.csv"
dfActeurs= pd.read_csv(fileActeurs, sep=';')
#print(dfActeurs)
print(len(dfActeurs))
listeActeurs=dfActeurs.Actors
firstLine=listeActeurs[0]

#print(listeActeurs[356])
#print(listeActeurs[453])
listeActeursF=[]
listeActeursFinal=[]
resRegex=[]
"""for i in range(len(listeActeurs)):
    if(i!=356 and i != 453 and i!= 642 and i!= 724 and i!= 778 and i!=830
       and i!= 878 and i!=970):
        line = listeActeurs[i]
        print(line)
        resRegex= line.split(",")
        
        for j in range(len(resRegex)): # ajout de tous les acteurs dans la liste
            if resRegex[j] not in listeActeursF:
                listeActeursF.append(resRegex[j])"""
                
        #listeActeursFinal.append(listeActeursF)
            
for i in range(len(dfActeurs)):
     if(i!=356 and i != 453 and i!= 642 and i!= 724 and i!= 778 and i!=830
     and i!= 878 and i!=970):
        line=listeActeurs[i]
        l=line.split(",")
        for j in range(len(l)):
            if (j==0):
                print("grahe avec 2 3 4")
            elif (j==1):
                print("grahe avec 1 3 4")
            elif (j==2):
                print("grahe avec 1 2 4")
            elif (j==3):
                print("grahe avec 1 2 3")
                
                
G=nx.Graph()
#G.add_node(1)
#H=nx.path_graph(10)
#G.add_nodes_from(H)

"""G.add_edge("Driss","Abdelhak","Rachid")
G.add_edge("Youssef","Rachid")
#H=nx.DiGraph(G)   # create a DiGraph using the connections from G
#H.edges()

nx.draw(G)
#nx.draw(H)
plt.show()        """
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    """isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }"""

#print(generate_edges(graph))
"""dot = Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
dot.render('test-output/round-table.gv', view=True)"""


#print(listeActeursF)        
#print(len(listeActeursF))
#print(listeActeursFinal)
#print(firstLine)
#print(firstLine)

"""reader=csv.reader(fileActeurs)
for row in reader :
    print(row)"""

#print(dfActeurs)