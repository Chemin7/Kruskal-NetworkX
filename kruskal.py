import networkx as nx
import matplotlib.pyplot as plt
import random
G=nx.Graph()

for node in range(9):
    G.add_node(node)

for node in range(9):
    for edge in range(4):
        G.add_edge(node,random.choice([i for i in range(1,10) if i not in [node]]),weight = random.randint(5,50))

pos=nx.spring_layout(G)
plt.figure()
nx.draw(G,pos,with_labels=True)
labels=nx.get_edge_attributes(G,"weight")

nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

edge_list = nx.get_edge_attributes(G,"weight")


edge_list = dict(sorted(edge_list.items(), key=lambda item: item[1]))


def getParent(dict_n,node):
    if dict_n[node][0] == -1:
        return node
    else:
        return getParent(dict_n,dict_n[node][0])
def Kruskal(edgeList,nodes):
    K = nx.Graph()
    K.add_nodes_from(nodes)
    dict_nodes = {}

    for key in nodes:

        dict_nodes[key] = [-1,0]
    

    num_edges = 0
    
    cond  = (edge for edge in edgeList if num_edges < K.number_of_nodes() - 1)
    for edge in cond:
        
        edge1 = edge[0]
        edge2 = edge[1]
        edge1_par = getParent(dict_nodes,edge1)
        edge2_par = getParent(dict_nodes,edge2)
        
        if(edge1_par != edge2_par):
            
            rank1 = dict_nodes[edge1][1]
            rank2 = dict_nodes[edge2][1]
            if(rank2 >  rank1):
                dict_nodes[edge1_par][0] = edge2_par
            elif rank1 > rank2:
                dict_nodes[edge2_par][0] = edge1_par
            else:
                dict_nodes[edge1_par][0] = edge2_par
                dict_nodes[edge2_par][1] += 1

            K.add_edge(edge1,edge2,weight =edgeList[edge])
            num_edges += 1
    for edge in edge_list:
        if not edge in K.edges():
            G.remove_edge(*edge)

    plt.figure()
    nx.draw(G,pos,with_labels=True)
    labels=nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.show()
    

Kruskal(edge_list,G.nodes)


for edge in G.edges():
    print(edge)


