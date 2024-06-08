import heapq
from typing import Dict, Tuple

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:

    priority_queue = [(0, start)]
    distances = {start: 0}
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 3, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'B'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)