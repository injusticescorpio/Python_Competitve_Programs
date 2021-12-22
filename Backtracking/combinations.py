def combinations(nums):
    res=[]
    comb=[]
    k=2
    def combs(i):
        if len(comb)==k:
            res.append(comb[:])
            return
        for i in range(i,len(nums)):
            print(f"i=={i}")
            comb.append(nums[i])
            combs(i+1)
            comb.pop()
        return res

    combs(0)
    print(res)
combinations([1,2,3])