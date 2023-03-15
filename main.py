import networkx as nx
import matplotlib.pyplot as plt

# Cria um grafo vazio
G = nx.Graph()

# Adiciona 10 vértices que representam pessoas com habilidades
G.add_node(1, name='Pessoa 1', habilidades=['Habilidade 1', 'Habilidade 2'])
G.add_node(2, name='Pessoa 2', habilidades=['Habilidade 2', 'Habilidade 3'])
G.add_node(3, name='Pessoa 3', habilidades=['Habilidade 1', 'Habilidade 4'])
G.add_node(4, name='Pessoa 4', habilidades=['Habilidade 5'])
G.add_node(5, name='Pessoa 5', habilidades=['Habilidade 3', 'Habilidade 4'])
G.add_node(6, name='Pessoa 6', habilidades=['Habilidade 1'])
G.add_node(7, name='Pessoa 7', habilidades=['Habilidade 2', 'Habilidade 4'])
G.add_node(8, name='Pessoa 8', habilidades=['Habilidade 1', 'Habilidade 3'])
G.add_node(9, name='Pessoa 9', habilidades=['Habilidade 2', 'Habilidade 5'])
G.add_node(10, name='Pessoa 10', habilidades=['Habilidade 3'])

# Adiciona algumas arestas aleatórias para criar conexões entre os vértices
G.add_edge(1, 2)
G.add_edge(3, 5)
G.add_edge(5, 6)
G.add_edge(7, 8)
G.add_edge(9, 10)

# Define as posições dos vértices para plotar o grafo
pos = nx.spring_layout(G)

# Cria uma lista de cores para plotar os vértices de acordo com suas habilidades
color_map = []
for node in G.nodes:
    habilidades = G.nodes[node]['habilidades']
    if 'Habilidade 1' in habilidades:
        color_map.append('red')
    elif 'Habilidade 2' in habilidades:
        color_map.append('blue')
    elif 'Habilidade 3' in habilidades:
        color_map.append('green')
    elif 'Habilidade 4' in habilidades:
        color_map.append('orange')
    else:
        color_map.append('gray')

# Plota o grafo com as cores dos vértices definidas acima
nx.draw(G, pos, node_color=color_map, with_labels=True)
plt.show()
