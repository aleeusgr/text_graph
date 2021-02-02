# export to gephi
from text import txt_pipe
import networkx as nx

#source = 'dream.txt'
source = 'short.txt'

nodes, grams = txt_pipe(source)
# mistake!(?? still works) not using BAG.

def graph():
    # create and the graph:
    G = nx.Graph()
    G.add_nodes_from(nodes)
    # edges from ngrams:
    for i in grams:
        l = len(i)
        for w in range(1,l-1):
            G.add_edge(i[0],i[w],weight=l-w)
    return G

G = graph()
#nx.write_gexf(G, "{}.gexf".format(source)) 

def vis():
    '''Visualise'''
    # for edge thickness:

    edges = G.edges
    weights = [G[u][v]['weight'] for u,v in edges]

    import matplotlib.pyplot as plt
    
    # Color nodes by POS tag
    import matplotlib.colors as mcolors
    color_list = mcolors.XKCD_COLORS
    tags = [u[1] for u in G.nodes(data="POS")]
    color_map = dict(zip(set(tags),color_list))
    colors =  [color_map[u[1]] for u in G.nodes(data='POS')]

    nx.draw(G, with_labels=True,width=weights,node_color = colors)
    plt.show()

#vis()
