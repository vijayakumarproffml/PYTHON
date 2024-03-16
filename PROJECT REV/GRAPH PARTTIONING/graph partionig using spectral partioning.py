import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def spectral_partitioning(G, num_partitions):
    # Compute the Laplacian matrix
    L = nx.laplacian_matrix(G).toarray()
    
    # Compute the eigenvectors corresponding to the smallest eigenvalues
    eigenvalues, eigenvectors = np.linalg.eigh(L)
    smallest_indices = np.argsort(eigenvalues)[:num_partitions]
    partition_vectors = eigenvectors[:, smallest_indices]
    
    # Use k-means clustering to partition the nodes based on the eigenvectors
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=num_partitions, random_state=0)
    partition_labels = kmeans.fit_predict(partition_vectors)
    
    return partition_labels

def visualize_partitioned_graph(G, partition_labels):
    pos = nx.spring_layout(G)
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'orange', 'pink', 'lime', 'purple']
    partition_color_map = {i: colors[partition_labels[i]] for i in range(len(partition_labels))}
    node_colors = [partition_color_map[i] for i in range(len(G.nodes))]
    
    nx.draw(G, pos, node_color=node_colors, with_labels=True)
    plt.show()

# Example usage
G = nx.karate_club_graph()
num_partitions = 9  # Adjust the number of partitions here
partition_labels = spectral_partitioning(G, num_partitions)
visualize_partitioned_graph(G, partition_labels)
