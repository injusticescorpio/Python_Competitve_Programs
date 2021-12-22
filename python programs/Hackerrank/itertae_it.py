def iterateIt(a):
    rep=0
    try:
        while a!=[]:
            b=[]
            for x in a:
                for y in a:
                    if x!=y:
                        b.append(abs(x-y))
            a=b
            rep+=1
            print(rep)

    except:
        return rep+1
    if a==[]:
        return rep
    else:
        return -1

n=int(input())
a=list(map(int,input().split(' ')))
print(iterateIt(a))
