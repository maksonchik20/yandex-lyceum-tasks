def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return [start, goal]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return

def create_base_graph(n, m):
    graph = {}
    all = list(range(1, n + 1)) * 10
    for now in range(0, n):
        graph[str(now + 1)] = set()
        for i in range(1, m + 1):
            graph[str(now + 1)].add(str(all[now + i]))
            graph[str(now + 1)].add(str(all[now - i]))
        graph[str(now + 1)] = list(graph[str(now + 1)])
    return graph


graph = create_base_graph(10, 2)
# print(graph)
print(BFS_SP(graph, '2', '6'))
# n, m, k = map(int, input().split())
# graph = create_base_graph(n, m)
# _max = 0
# for i in range(1, n + 1):
#     flag = False
#     for j in range(1, n + 1):
#         res = BFS_SP(graph, str(i), str(j))
#         if res is None:
#             print(n)
#             flag = True
#             break
#         _max = max(len(res) - 2, _max) 
#     if flag:
#         break
# if not flag:
#     print(_max)
# for _ in range(k):
#     _max = 0
#     a, x, y = input().split()
#     if a == '1':
#         if y not in graph[x]:
#             graph[x].append(y)
#             graph[y].append(x)
#     elif a == '0':
#         try:
#             graph[x].remove(y)
#         except ValueError:
#             pass
#         try:
#             graph[y].remove(x)
#         except ValueError:
#             pass
#     for i in range(1, n + 1):
#         flag = False
#         for j in range(1, n + 1):
#             res = BFS_SP(graph, str(i), str(j))
#             if res is None:
#                 print(n)
#                 flag = True
#                 break
#             _max = max(len(res) - 2, _max) 
#         if flag:
#             break
#     if not flag:
#         print(_max)
