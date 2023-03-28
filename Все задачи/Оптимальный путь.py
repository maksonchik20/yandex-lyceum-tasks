from math import inf
from sys import setrecursionlimit, stdin
# setrecursionlimit(10**6)




# # graph = {}

# # for line in stdin:
# #     line = line.strip().split()
# #     if len(line) == 2:
# #         a, b = line
# #     else:
# #         from_path, to_path, weight = line
# #         weight = int(weight)
# #         if graph.get(from_path) is not None:
# #             graph[from_path].append((to_path, weight))
# #         else:
# #             graph[from_path] = [(to_path, weight)]
# #         if graph.get(to_path) is not None:
# #             graph[to_path].append((from_path, weight))
# #         else:
# #             graph[to_path] = [(from_path, weight)]

# # print(graph)
# graph = {'1': [('2', 10)], '2': [('1', 10), ('5', 6), ('3', 1)], '5': [('2', 6), ('4', 2)], '3': [('2', 1), ('4', 1)], '4': [('3', 1), ('5', 2)]}
# def get_weight(a, b):
#     if a == b:
#         return 0
#     for el in graph[a]:
#         if el[0] == b:
#             return el[1]
#     return inf

# def all_path(a):
#     result = []
#     for i in graph[a]:
#         result.append(i[0])
#     return result

# # cnt = 0
# # path = ""
# # bil = set()
# # def deikstra(a, b, pr=None):
# #     global path
# #     global cnt
# #     if a == b:
# #         return 0
# #     _min = inf
    
# #     local_path = ""
# #     for i in all_path(b):
# #         if pr is not None:
# #             if i == pr:
# #                 continue
# #         if i in bil:
# #             continue
# #         weight = deikstra(a, i, pr=b) + get_weight(i, b)
# #         if weight < _min:
# #             _min = weight
# #             local_path = i
# #         bil.add(i)
# #     cnt += _min
# #     path += local_path
# #     return _min
    
    

# graph = {
#     '1': [('2', 2), ('3', 10)],
#     '2': [('3', 1), ('1', 2)],
#     '3': [('2', 1), ('1', 10)]
# }


# def way(a, b):
#     _min = inf
#     for i in all_path(b):
#         path = BFS_SP(a, i)
#         for i in range(1, len(path)):
#             ...
#         if path :

# a, b = '1', '5'
# print(way(a, b))
# # print(deikstra(a, b))
# # path += b
# bil = set()
# # for p in path:
# #     if p in  bil:
# #         continue
# #     print(p, end=' ')
# #     bil.add(p)

# Алгоритм



# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : [],
#   'D' : [],
#   'E' : []
# }

def get_weight(graph, a, b):
    if a == b:
        return 0
    for el in graph[a]:
        if el[0] == b:
            return el[1]
    return inf

def all_path(a):
    result = []
    for i in graph[a]:
        result.append(i[0])
    return result

# graph = {}

# for line in stdin:
#     line = line.strip().split()
#     if len(line) == 2:
#         a, b = line
#     else:
#         from_path, to_path, weight = line
#         weight = int(weight)
#         if graph.get(from_path) is not None:
#             graph[from_path].add((to_path, weight))
#         else:
#             graph[from_path] = {(to_path, weight)}
#         if graph.get(to_path) is not None:
#             graph[to_path].add((from_path, weight))
#         else:
#             graph[to_path] = {(from_path, weight)}

# print(graph)
result = []


def way(graph, a, b, visited):
    _min = 10 ** 8
    path = ""
    if a == b:
        return 0
    for el in all_path(b):
        if el not in visited:
            visited.add(b)
            # _min_copy = _min
            # prev_res = way(graph, a, el, visited) + get_weight(graph, b, el)
            _min = min(_min, way(graph, a, el, visited) + get_weight(graph, b, el))
            # del prev_res
            # if _min != _min_copy:
            #     path = el
            # del _min_copy
    # result.append(path)
    # del path
    return _min
graph = {'1': {('3', 9), ('2', 7), ('6', 14)}, '2': {('4', 15), ('3', 10), ('1', 7)}, '3': {('1', 9), ('2', 10), ('6', 2), ('4', 11)}, '6': {('1', 14), ('3', 2), ('5', 9)}, '4':
{('2', 15), ('5', 6), ('3', 11)}, '5': {('4', 6), ('6', 9)}}

# a, b = '1', '4'
# print(way(graph, a, b, set()))
print(way(graph, '1', '4', set()))
# print(all_path('4'))
# result.append(b)
# result = filter(lambda x: x != "", result)
# print(", ".join(result))

