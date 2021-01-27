# POS tags as node attributes
# export to gephi
from text import txt_pipe
import networkx as nx

source = 'dream.txt'
source = 'short.txt'

# try to: bag = [(lemmatized,POS_tag),]
bag, grams = txt_pipe(source)
# mistake!(?? still works) not using BAG.
print(bag)

def vis():
    # create and vis the graph:
    G = nx.Graph()
    G.add_nodes_from(bag)
    # edges from ngrams:
    for i in grams:
        l = len(i)
        for w in range(1,l-1):
            G.add_edge(i[0],i[w],weight=l-w)
    
    # for edge thickness:
    edges = G.edges
    weights = [G[u][v]['weight'] for u,v in edges]

    import matplotlib.pyplot as plt
    nx.draw(G, with_labels=True,width=weights)
    plt.show()

#vis()
