def stepPerms(n):
    a=[1,2,3]
    res=[]
    comb=[]
    cache={}
    def dfs(k):
        print(comb)
        if sum(comb)==n:
            res.append(1)
            return
        if sum(comb)>n:
            return

        for i in range(0,len(a)):
            comb.append(a[i])
            dfs()
            comb.pop()
    dfs(0)
    return sum(res)

print(stepPerms(5))