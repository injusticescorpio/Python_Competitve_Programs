def main(n,c,k):
    res=[]
    part=[]
    c=[i for i in range(1,c+1)]
    def dfs():
        if len(part)==n:
            count=0
            for i in range(len(part)-1):
                if part[i]!=part[i+1]:
                    count+=1
            if count==k:
                res.append(part[:])
            return
        for i in range(0,len(c)):
            part.append(c[i])
            dfs()
            part.pop()
    dfs()
    print(len(res))
n=int(input())
color=int(input())
k=int(input())
main(n,color,k)
