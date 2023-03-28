def recursive_len(some_list, cnt=1):
    if some_list == []:
        return 0
    return recursive_len(some_list[:-1], cnt) + cnt
