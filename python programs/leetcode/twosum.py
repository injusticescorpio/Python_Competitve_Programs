# 2,7,11,15
nums=list(map(int,input().split(',')))
target=int(input())
i=0
j=len(nums)-1
while(i<len(nums)):
    if nums[i]+nums[j]==target:
        print(f"i=={i} and j=={j}")
        break
    else:
        if nums[i]<=nums[j] and nums[j]>target:
            i+=1
        else:
            j-=1
