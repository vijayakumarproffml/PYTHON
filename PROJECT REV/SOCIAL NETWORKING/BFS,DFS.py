import time
import queue
import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

file = "D:/PYTHON/PROJECT REV/SOCIAL NETWORKING/realationship.xml"

G = nx.Graph()
names = []

Tree = ET.parse(file)
Root = Tree.getroot()

for item in Root.iter("relationship"):
    person1 = item.attrib["person1"]
    person2 = item.attrib["person2"]
    gender1 = item.attrib["gender1"]
    gender2 = item.attrib["gender2"]

    G.add_node(person1, gender=gender1)
    G.add_node(person2, gender=gender2)

    names.append((person1, person2))

color_map = nx.get_node_attributes(G, "gender")

for key in color_map:
    if color_map[key] == "male":
        color_map[key] = 'blue'

    if color_map[key] == "female":
        color_map[key] = "pink"

gender_color = [color_map.get(node) for node in G.nodes()]

G.add_edges_from(names)
pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
nx.draw(G, pos, with_labels=True, node_color=gender_color, node_size=500)
plt.title('SOCIAL NETWORK')
plt.pause(1)
plt.show()



def order_bfs(graph, start_node):
    visited = set()
    order = []
    q = queue.Queue()
    q.put(start_node)

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            for node in graph.neighbors(vertex):
                if node not in visited:
                    q.put(node)
    return order


def order_dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    order = []

    if start_node not in visited:
        visited.add(start_node)
        order.append(start_node)
        for node in graph.neighbors(start_node):
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))

    return order
def visualization(order,title,G,pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order,start=1):
        plt.clf()
        plt.title(title)
    nx.draw(G,pos,with_labels=True,node_color=['r' if n==node else 'blue' for n in G.nodes()])
    plt.show()
    plt.pause(2)
    time.sleep(0.5)
    
    
    
pos=nx.spring_layout(G)
    
visualization(order_bfs(G,"vijay"),"BFS VISUALIZATION",G,pos)
visualization(order_dfs(G,"vijay"),"DFS VISUALIZATION",G,pos)
    
                