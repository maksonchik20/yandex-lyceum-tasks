def recursive_reverse(some_list):
    if some_list == []:
        return []
    return [some_list[-1]] + recursive_reverse(some_list[:-1])


print(recursive_reverse([]))