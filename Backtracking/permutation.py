#input=[1,2,3]
#output=[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[[3,1,2],[3,2,1]


def permute(nums):
    result=[]
    if len(nums)==1:
        return [nums[:]]
    for i in range(0,len(nums)):
        n=nums.pop(0)
        perms=permute(nums)
        print(f"perms={perms}")
        print(f"res1=={result}")
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        print(f"res={result}")
        nums.append(n)
    return result

print(permute([1,2,3]))