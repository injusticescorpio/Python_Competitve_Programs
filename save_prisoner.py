def saveThePrisoner(n, m, s):
    t=[i for i in range(1,n+1)]
    print(t[0])
    res=[]
    s-=1
    print(n)
    for i in range(0,m):
        print(f"{s}%{n}=={s%n}")
        res.append(t[s%n])
        s+=1
    print(res)
saveThePrisoner(7,19,2)