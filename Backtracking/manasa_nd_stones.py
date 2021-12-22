def main():
    arr=[10,100]
    res=[]
    comb=[0]
    n=4
    def dfs():
        if comb[-1] in res:
            return

        if len(comb)==n:
            res.append(comb[-1])
            return
        for i in range(0,len(arr)):
            comb.append(comb[-1]+arr[i])
            dfs()
            comb.pop()
    dfs()
    print(res)
main()