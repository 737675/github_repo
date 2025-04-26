#Shorted Path Finder using Djkastra's Algoritham

import heapq

def dijkstra(graph, start, end):
    heap = [(0, start, [start])]  # (total_cost, current_city, path_taken)
    visited = set()

    while heap:
        cost, city, path = heapq.heappop(heap)

        if city == end:
            return path, cost

        if city in visited:
            continue
        visited.add(city)

        for neighbor, weight in graph[city].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')  # if path not found

# Example Input
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

path, total_distance = dijkstra(cities, start_city, destination_city)

print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
print(f"Total distance: {total_distance}")
