# from functools import lru_cache 
 
# @lru_cache(maxsize=None) 
# def solve(n): 
#     if n <= 2: 
#         return 1 
#     result = 0 
#     for i in range(2, min(int(n ** .5), m) + 1): 
#         if n % i == 0: 
#             result += solve(i) 
#             if i * i != n: 
#                 result += solve(n // i) 
#     return result 
 
# n, m = map(int, input().split()) 
# print(solve(n) + (n == m))

# from functools import lru_cache 
 
# @lru_cache(maxsize=None) 
# def solve(n, prev): 
#     if n <= 2: 
#         return 1 
#     result = 0 
#     for i in range(2, prev): 
#         if n % i == 0: 
#             result += solve(n // i, i) 
#     return result 
 
# n, m = map(int, input().split()) 
# print(solve(n, m + 1))

# from sympy import divisors, isprime 
# from functools import lru_cache 
# @lru_cache(maxsize=None) 
# def solve(n, prev): 
#     if n <= 2: 
#         return 1 
#     result = 0 
#     for i in range(2, prev + 1): 
#         if n % i == 0: 
#             result += solve(n // i, i) 
#     return result 
# n, m = map(int, input().split()) 
# print(solve(n, m + 1))
 
# from random import randint 
# for _ in range(1000): 
#     n = randint(1, 1000000) 
#     m = randint(1, n) 
#     a = solve(n, m) 
#     b = T(n, m) 
#     print(a == b, a, b)


from functools import lru_cache

@lru_cache(maxsize=None, typed=False)
def solve(n, m, i = 2):
    if n < i:
        return 0
    result = int(n <= m)
    while i ** 2 <= n and i <= m:
        if n % i == 0:
            result += solve(n // i, m, i)
        i += 1
    return result

print(solve(*map(int, input().split())))