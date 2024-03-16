import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edges_from([(1,2),(2,3),(3,4),(3,5),(4,6),(6,7),(2,8),(8,9),(9,4)])

# Fixed position of nodes using spring layout
pos = nx.spring_layout(G)


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
            nx.draw(graph, pos=pos, with_labels=True, node_color=['red' if n == node else 'skyblue' for n in graph.nodes()], node_size=700)
            plt.title('BFS Traversal')
            plt.pause(1)
            plt.clf()

# Breadth-First Search  Shortest Path(BFS)
def bfs_path(graph, start, end):
    visited = set()
    queue = [(start, [start])]

    while queue:
        node, path = queue.pop(0)
        if node not in visited:
            if node == end:
                return path
            visited.add(node)
            neighbors = graph.neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

            # Visualization: Highlight the visited node
            nx.draw(graph, pos=pos, with_labels=True, node_color=['red' if n == node else 'skyblue' for n in graph.nodes()], node_size=700)
            plt.title('SHORTEST PATH')
            plt.pause(1)
            plt.clf()

    return None

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    # Visualization: Highlight the visited node
    nx.draw(graph, pos=pos, with_labels=True, node_color=['red' if n == start else 'skyblue' for n in graph.nodes()], node_size=700)
    plt.title('DFS Traversal')
    plt.pause(1)
    plt.clf()

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


print("BFS Traversal:")
bfs(G, 1)  # Start BFS from node 1
print()
print("SHORTEST PATH:")
bfs_path = bfs_path(G, 1, 7)  # Start BFS from node 1 to find shortest path to node 7
print("Shortest Path from 1 to 7:", bfs_path)



print("\n\nDFS Traversal:")
dfs(G, 1)  # Start DFS from node 1
