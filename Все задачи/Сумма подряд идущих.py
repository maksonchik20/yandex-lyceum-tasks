from itertools import accumulate
from math import sqrt
n, cnt = int(input()), 0
d = (int( sqrt( (8 * n + 1) ) ) - 1) // 2
for ind, el in enumerate(accumulate(range(1, d + 1)), 1):
    cnt += 1 if (n - el) % ind == 0 else 0
print(cnt)
