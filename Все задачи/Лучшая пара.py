n, p = map(int, input().split())
nums = list(map(lambda x: int(x) % p ,input().split()))

for i in range(p - 1, 0, -1):
    flag = False
    for j in range(n):
        if nums[j] - i in nums:
            print(nums.index(nums[j] - i) + 1, j + 1)
            flag = True
            break
        elif i - nums[j] in nums:
            print(nums.index(i - nums[j]) + 1, j + 1)
            flag = True
            break
    if flag:
        break
