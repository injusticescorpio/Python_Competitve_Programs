def main():
    li=[1,2,3]
    comb=[]
    n=5
    res=[]
    def dfs(comb):
        if sum(comb)==n:
            res.append(1)
            return
        elif sum(comb)>n:
             return
        for i in range(0,len(li)):
            comb.append(li[i])
            dfs(comb)
            comb.pop()
    dfs(comb)
    print(sum(res))
main()

