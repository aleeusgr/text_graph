# export to gephi
from text import txt_pipe
import networkx as nx

source = 'dream.txt'
source = 'short.txt'

nodes, grams = txt_pipe(source)
# mistake!(?? still works) not using BAG.

def graph():
    # create and vis the graph:
    G = nx.Graph()
    G.add_nodes_from(nodes)
    # edges from ngrams:
    for i in grams:
        l = len(i)
        for w in range(1,l-1):
            G.add_edge(i[0],i[w],weight=l-w)
    return G

G = graph()

def vis():
    
    # for edge thickness:
    edges = G.edges
    weights = [G[u][v]['weight'] for u,v in edges]

    import matplotlib.pyplot as plt

#vis()
    import matplotlib.colors as mcolors
    color_list = mcolors.cnames.keys()
    tags = [u[1] for u in G.nodes(data="POS")]
    color_map = dict(zip(set(tags),color_list))
    colors =  [color_map[u[1]] for u in G.nodes(data='POS')]

    nx.draw(G, with_labels=True,width=weights,node_color = colors)
    plt.show()
# convert node POS tag into collection, assign color 

vis()
