# # from collections import Counter
# # from sys import setrecursionlimit
# # n = int(input())
# # data = Counter(list(map(int, input().split())))
# # result_cnt = 0
# # setrecursionlimit(10_000_000)
# # def get_max(data, now_cnt):
# #     global result_cnt
# #     for el in +data:
# #         data2 = +data
# #         if data2[el] > 0:
# #             data2[el] = data2[el] - 1
# #             now_cnt += el
# #             data2[el + 1] = 0
# #             data2[el - 1] = 0
# #             if len(+data2) == 0:
# #                 result_cnt = max(now_cnt, result_cnt)
# #                 now_cnt = 0
# #                 continue
# #             get_max(+data2, now_cnt)
# #             now_cnt = 0
# #     return result_cnt

# # print(get_max(data, result_cnt))



# from collections import Counter
# from sys import setrecursionlimit
# n = int(input())
# data = Counter(list(map(int, input().split())))

n = int(input())
data = list(map(int,input().split()))
_max = max(data)+1
ans = [0] * _max
for a in data:
    ans[a] += 1
for i in range(2, _max):
    ans[i] = max(ans[i - 1], ans[i - 2] + ans[i] * i)
print(max(ans))

# _, t, count = input(), {}, 0
# for v in map(int, input().split()): t[v] = t.get(v, 0) + 1
# while len(t):
#   v = sorted([[-t.get(v - 1, 0) - t.get(v + 1, 0), v] for v in t])[-1][1]
#   count += v
#   t.pop(v - 1, 0)
#   t.pop(v + 1, 0)
#   t[v] -= 1
#   if t[v] == 0: t.pop(v)
# print(count)