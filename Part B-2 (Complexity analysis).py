# Complexity analysis
import time
import random
import networkx as nx
import matplotlib.pyplot as plt

def create_random_graph(num_vertices, edge_probability):
    """
    Create a random graph with the given number of vertices and edge probability.

    Args:
        num_vertices (int): Number of vertices in the graph.
        edge_probability (float): Probability of an edge between any two vertices.

    Returns:
        nx.Graph: A random graph.
    """
    G = nx.Graph()
    for i in range(num_vertices):
        G.add_node(i)
        for j in range(i + 1, num_vertices):
            if random.random() < edge_probability:
                G.add_edge(i, j, weight=random.uniform(1, 10))  # Assign random weights to edges
    return G

def measure_time_complexity(num_vertices_list, edge_probability):
    """
    Measure the time complexity of adding vertices, adding edges, and finding shortest paths
    on graphs with varying numbers of vertices.

    Args:
        num_vertices_list (list): List of number of vertices to test.
        edge_probability (float): Probability of an edge between any two vertices.
    """
    add_vertex_times = []
    add_edge_times = []
    shortest_path_times = []

    for num_vertices in num_vertices_list:
        # Create a random graph with the specified number of vertices
        G = create_random_graph(num_vertices, edge_probability)

        # Measure time for adding vertices
        start_time = time.time()
        G.add_node(num_vertices + 1)  # Adding one more vertex
        add_vertex_times.append(time.time() - start_time)

        # Measure time for adding edges
        start_time = time.time()
        u, v = random.sample(range(num_vertices), 2)  # Select two random vertices
        G.add_edge(u, v, weight=random.uniform(1, 10))  # Adding an edge between them
        add_edge_times.append(time.time() - start_time)

        # Measure time for finding shortest path
        start_time = time.time()
        source, target = random.sample(range(num_vertices), 2)  # Select two random vertices
        nx.shortest_path_length(G, source=source, target=target, weight='weight')  # Find shortest path length
        shortest_path_times.append(time.time() - start_time)

    return add_vertex_times, add_edge_times, shortest_path_times

# Parameters
num_vertices_list = [100, 200, 300, 400, 500]  # Varying number of vertices
edge_probability = 0.2  # Probability of an edge between any two vertices

# Measure time complexity
add_vertex_times, add_edge_times, shortest_path_times = measure_time_complexity(num_vertices_list, edge_probability)

# Plotting results
plt.plot(num_vertices_list, add_vertex_times, label='Add Vertex')
plt.plot(num_vertices_list, add_edge_times, label='Add Edge')
plt.plot(num_vertices_list, shortest_path_times, label='Shortest Path')
plt.xlabel('Number of Vertices')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Analysis')
plt.legend()
plt.show()


