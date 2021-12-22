def product(a,res=[],v=0,p=[]):
    print(f"a=={a}")
    print(f"res=={res}")
    if a==[]:
        return res
    for i in a[0]:
        print(f"a[0]=={a[0]}")
        res=a
        if a[2]==None:
            b=a[1]
            print(f"b=={b}")
        else:
            if v==0:
                b=product(a[1:],res,v)
                print(f"b=={b}")
        if b==None:
            v=1
            print(f"b=={b}")
            b=p[:]
            print(f"after b=={b}")
        for j in b:
            p.append([i]+[j])
            print(f"p=={p}")


a=[[1,2],[3,4],[5,6 ],[8,9],None]
print(product(a))
