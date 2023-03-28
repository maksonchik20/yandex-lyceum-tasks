# def linear(some_list, result=[]):
#     if some_list == []:
#         return result
#     if type(some_list[0]) is list:
#         result.extend(linear(some_list[0], result=[]))
#     else:
#         result.append(some_list[0])
#     return linear(some_list[1:], result)

def linear(some_list):
    if some_list == []:
        return some_list
    if isinstance(some_list[0], list):
        return linear(some_list[0]) + linear(some_list[1:])
    return [some_list[0]] + linear(some_list[1:])

# print(linear(linear( [[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]] )))

# assert linear([]) == []
assert linear(linear([[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]])) == [1, 2, 4, 2, 4, 8, -4, 'er', 0, {2: 'primer'}]