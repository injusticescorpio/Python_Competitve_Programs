def main(a,n):
    res=[]
    comb=[]
    print(a)
    print(n)
    def dfs():
        if sum(comb)==n:
            if sorted(comb) not in res:
                res.append(sorted(comb))
                print(res)
            return
        elif sum(comb)>n:
            return
        for i in range(0,len(a)):
            comb.append(a[i])
            dfs()
            comb.pop()
    dfs()
    print(len(res))
n=166
a=list(map(int,input().split(' ')))
print(n)
main(a,n)

