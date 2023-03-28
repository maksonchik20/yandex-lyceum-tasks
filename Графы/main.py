from collections import defaultdict
import heapq

graph = {
    '1': [('4', 1), ('2', 1)],
    '2': [('5', 1), ('1', 1)],
    '3': [('6', 1)],
    '4': [],
    '5': [],
    '6': [('2', 1), ('3', 1)]
}
# У каждого два друга.


def dijkstra(graph, start: str):
    result_map = defaultdict(lambda: float('inf'))
    result_map[start] = 0

    visited = set()

    queue = [(0, start)]

    while queue:
        weight, v = heapq.heappop(queue)
        visited.add(v)

        for u, w in graph[v]:
            if u not in visited:
                result_map[u] = min(w + weight, result_map[u])
                heapq.heappush(queue, [w + weight, u])

    return result_map
print(dijkstra(graph=graph, start='1'))


