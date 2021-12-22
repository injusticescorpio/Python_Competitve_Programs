nums=list(map(int,input().split(' ')))
res = [0] * len(nums)
res[0] = nums[0]
for i in range(1, len(nums)):
    j = i
    s = 0
    while (j != -1):
        s += nums[j]
        j-=1
    res[i] = s
print(res)