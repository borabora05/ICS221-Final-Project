#Represent the road network using a graph
class RoadNetwork:
    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices (intersections)
        self.edges = []     # List to store edges (roads)

    def add_vertex(self, vertex_id):
        """
        Add a vertex (intersection) to the road network.

        Args:
            vertex_id (int): The ID of the intersection.
        """
        self.vertices[vertex_id] = {}

    def add_road(self, road_id, start_vertex, end_vertex, road_name, road_length):
        """
        Add a road (edge) to the road network.

        Args:
            road_id (int): The ID of the road.
            start_vertex (int): The ID of the starting intersection.
            end_vertex (int): The ID of the ending intersection.
            road_name (str): The name of the road.
            road_length (float): The length of the road.
        """
        self.edges.append((road_id, start_vertex, end_vertex, road_name, road_length))
        # Add road to both start and end vertices
        self.vertices[start_vertex][end_vertex] = road_length
        self.vertices[end_vertex][start_vertex] = road_length

#..........................................
# Model package distribution
class RoadNetworkWithHouses(RoadNetwork):
    def add_house(self, house_id, intersection_id):
        self.vertices[house_id] = {}
        self.vertices[house_id][intersection_id] = 0

    def distribute_packages(self, distribution_center_id):
        """
        Distribute packages from a distribution center to houses using Dijkstra's algorithm.

        Args:
            distribution_center_id (str): The ID of the distribution center (intersection).

        Returns:
            dict: Dictionary containing shortest paths from the distribution center to each house.
        """
        shortest_paths = {}
        # Apply Dijkstra's algorithm to find shortest paths
        # (Code for Dijkstra's algorithm implementation not included here for brevity)
        return shortest_paths

    def shortest_distance(self, start_vertex, end_vertex):
        """
        Find the shortest distance from point A to point B using Dijkstra's algorithm.

        Args:
            start_vertex (str): The ID of the starting intersection.
            end_vertex (str): The ID of the ending intersection.

        Returns:
            float: The shortest distance between the start and end vertices.
        """
        # Apply Dijkstra's algorithm to find the shortest distance
        # (Code for Dijkstra's algorithm implementation not included here for brevity)
        shortest_distance = 10.0  # Placeholder for actual implementation
        return shortest_distance

#...........................................
# Shortest distance from point A to point B
def shortest_distance(self, start_vertex, end_vertex):
    """
    Find the shortest distance from point A to point B using Dijkstra's algorithm.

    Args:
        start_vertex (int): The ID of the starting intersection.
        end_vertex (int): The ID of the ending intersection.

    Returns:
        float: The shortest distance between the start and end vertices.
    """
    # Apply Dijkstra's algorithm to find the shortest distance
    # (Code for Dijkstra's algorithm implementation not included here for brevity)
    shortest_distance = 0.0  # Placeholder for actual implementation
    return shortest_distance
#........................................................
# Testing
# Create a road network
road_network = RoadNetwork()

# Add vertices (intersections)
road_network.add_vertex('A')
road_network.add_vertex('B')
road_network.add_vertex('C')

# Add roads (edges)
road_network.add_road('A', 'A', 'B', "Main Street", 5.3)
road_network.add_road('B', 'B', 'C', "Broadway", 3.8)
road_network.add_road('C', 'A', 'C', "Oak Avenue", 7.1)

# Display vertices and roads
print("Vertices:", road_network.vertices)
print("Roads:", road_network.edges)


# Create a road network with houses
road_network_with_houses = RoadNetworkWithHouses()

# Add vertices (intersections)
road_network_with_houses.add_vertex('A')
road_network_with_houses.add_vertex('B')
road_network_with_houses.add_vertex('C')

# Add roads (edges)
road_network_with_houses.add_road('A', 'A', 'B', "Main Street", 5.3)
road_network_with_houses.add_road('B', 'B', 'C', "Broadway", 3.8)
road_network_with_houses.add_road('C', 'A', 'C', "Oak Avenue", 7.1)

# Add houses
road_network_with_houses.add_house(101, 'A')
road_network_with_houses.add_house(102, 'B')
road_network_with_houses.add_house(103, 'C')

# Distribute packages from distribution center
distribution_center_id = 'A'
package_distribution = road_network_with_houses.distribute_packages(distribution_center_id)

# Display package distribution
if not package_distribution:
    print("There are no houses to distribute packages to from the distribution center.")
else:
    print("Package Distribution:", package_distribution)


# Find shortest distance between two points
start_vertex = 'A'
end_vertex = 'C'
shortest_distance = road_network_with_houses.shortest_distance(start_vertex, end_vertex)

# Display shortest distance
print("Shortest Distance from Point A to Point C:", shortest_distance, 'Units')

#............................................

import networkx as nx
import matplotlib.pyplot as plt

class RoadNetwork:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = {}

    def add_road(self, road_id, start_vertex, end_vertex, road_name, road_length):
        self.edges.append((road_id, start_vertex, end_vertex, road_name, road_length))
        self.vertices[start_vertex][end_vertex] = road_length
        self.vertices[end_vertex][start_vertex] = road_length

    def create_networkx_graph(self):
        G = nx.Graph()
        for vertex_id in self.vertices:
            G.add_node(vertex_id)
        for road_id, start_vertex, end_vertex, road_name, road_length in self.edges:
            G.add_edge(start_vertex, end_vertex, weight=road_length, road_name=road_name)
        return G

    def visualize_network(self):
        G = self.create_networkx_graph()
        pos = nx.spring_layout(G)  # positions for all nodes
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000)
        labels = nx.get_edge_attributes(G, 'road_name')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

class RoadNetworkWithHouses(RoadNetwork):
    def add_house(self, house_id, intersection_id):
        self.vertices[house_id] = {}
        self.vertices[house_id][intersection_id] = 0

    def create_networkx_graph(self):
        G = super().create_networkx_graph()
        for house_id in self.vertices:
            if house_id not in G.nodes:
                G.add_node(house_id)
        return G

# Example road network
road_network = RoadNetwork()
road_network.add_vertex('A')
road_network.add_vertex('B')
road_network.add_vertex('C')
road_network.add_road('A', 'A', 'B', "Main Street", 5.3)
road_network.add_road('B', 'B', 'C', "Broadway", 3.8)
road_network.add_road('C', 'A', 'C', "Oak Avenue", 7.1)

# Visualize road network
road_network.visualize_network()

