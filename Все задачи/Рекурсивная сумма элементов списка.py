from functools import lru_cache

@lru_cache(maxsize=128)
def rec_linear_sum(some_list, cnt):
    if some_list == []:
        return 0
    cnt += some_list[-1]
    return rec_linear_sum(some_list[:-1], cnt)


print(rec_linear_sum([]))