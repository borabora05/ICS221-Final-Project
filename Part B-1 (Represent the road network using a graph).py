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