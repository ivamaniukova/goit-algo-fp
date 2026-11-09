import heapq

def dijkstra(graph, start):
    if start not in graph:
        raise ValueError("Start node not in graph")

    for neightbors in graph.values():
        for weight in neightbors.values():
            if weight < 0:
                raise ValueError("Graph contains negative weight edges")

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1, "E": 10},
        "D": {"B": 5, "C": 1, "E": 2},
        "E": {"C": 3, "D": 2},
    }
    start = "A"
    distances = dijkstra(graph, start)
    print(f"Shortest distances from {start}:")
    for vertex, distance in distances.items():
        print(f"  {vertex}: {distance}")