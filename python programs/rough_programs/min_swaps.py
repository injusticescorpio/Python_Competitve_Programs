m=int(input())
a=[int(i) for i in input().split(' ')][:m]
print(f"a=={a}")
i=0
c=0
while(i<len(a)-1):
    print(f"i=={i}")
    print(f"a=={a}")
    print(a[i+1:])
    if a[i]>min(a[i+1:]):
        print(f"{a[i]}>{min(a[i+1:])}")
        b=a.index(min(a[i+1:]))
        print(f"index=={b}")
        a[i],a[b]=a[b],a[i]
        i+=1
        c+=1
    else:
        i+=1
print(f"c=={c}")



