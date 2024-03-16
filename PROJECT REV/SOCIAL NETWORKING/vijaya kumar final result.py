import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

file = "D:/PYTHON/PROJECT REV/SOCIAL NETWORKING/realationship.xml"

G = nx.Graph()
names = []
total_names=[]


Tree = ET.parse(file)
Root = Tree.getroot()

for item in Root.iter("relationship"):
    person1 = item.attrib["person1"]
    person2 = item.attrib["person2"]
    gender1 = item.attrib["gender1"]
    gender2 = item.attrib["gender2"]

    G.add_node(person1, gender=gender1)
    G.add_node(person2, gender=gender2)
    total_names.append(person1)
    total_names.append(person2)

    names.append((person1, person2))

color_map = nx.get_node_attributes(G, "gender")

for key in color_map:
    if color_map[key] == "male":
        color_map[key] = 'blue'

    if color_map[key] == "female":
        color_map[key] = "pink"

gender_color = [color_map.get(node) for node in G.nodes()]
node_sizes=[(total_names.count(node)*500) for node in G.nodes()]


G.add_edges_from(names)

pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
nx.draw(G, pos, with_labels=True, node_color=gender_color, node_size=node_sizes)
plt.title('SOCIAL NETWORK')
plt.pause(1.5)
plt.show()

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            neighbors = graph.neighbors(node)
            queue.extend(neighbors)

            # Visualization: Highlight the visited node
            nx.draw(graph, pos=pos, with_labels=True, node_color=['red' if n == node else 'skyblue' for n in graph.nodes()],node_size=node_sizes)
            plt.title(f'BFS Traversal: Visiting {node}')
            plt.pause(1)
            plt.clf()

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    # Visualization: Highlight the visited node
    nx.draw(graph, pos=pos, with_labels=True, node_color=['red' if n == start else 'skyblue' for n in graph.nodes()],node_size=node_sizes)
    plt.title(f'DFS Traversal: Visiting {start}')
    plt.pause(1)
    plt.clf()

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)




print("\n\n----> BFS Traversal <----")
bfs(G, "vijay")  # Start BFS from node vijay
print()


print("\n\n----> DFS Traversal <----")
dfs(G, "vijay")  # Start DFS from node vijay