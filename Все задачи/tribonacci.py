from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**7)

@lru_cache(maxsize=128)
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3) 
