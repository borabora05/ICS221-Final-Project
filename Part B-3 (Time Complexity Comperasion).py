import matplotlib.pyplot as plt

# Number of vertices (V) for complexity analysis
vertices = [10, 50, 100, 200, 500, 700, 850, 1000]

# Time complexities for basic road network (without houses)
basic_road_network_best_case = [(V * 0.1 * 0.1) for V in vertices]  # Best case: O(log V)
basic_road_network_worst_case = [(V + V * V) * (V * 0.1 * 0.1) for V in vertices]  # Worst case: O((V + V^2) log V)

# Time complexities for road network with houses
road_network_with_houses_best_case = [(V * 0.1 * 0.1) for V in vertices]  # Best case: O(log V)
road_network_with_houses_worst_case = [(V + V * V) * (V * 0.1 * 0.1) for V in vertices]  # Worst case: O((V + V^2) log V)

# Plotting
plt.figure(figsize=(10, 6))

# Basic road network
plt.plot(vertices, basic_road_network_best_case, label='Basic Road Network - Best Case (O(log V))', marker='o', color='blue')
plt.plot(vertices, basic_road_network_worst_case, label='Basic Road Network - Worst Case (O((V + V^2) log V))', marker='o', color='orange')

# Road network with houses
plt.plot(vertices, road_network_with_houses_best_case, label='Road Network with Houses - Best Case (O(log V))', marker='o', color='green')
plt.plot(vertices, road_network_with_houses_worst_case, label='Road Network with Houses - Worst Case (O((V + V^2) log V))', marker='o', color='red')

plt.title('Comparison of Time Complexities for Road Networks')
plt.xlabel('Number of Vertices (V)')
plt.ylabel('Time Complexity')
plt.grid(True)
plt.legend()
plt.xticks(vertices)

plt.show()
