a=list(map(int,input().split(' ')))
b=int(input())
c=[]
for i in range(0,len(a)-1):
    target = b
    j=i
    t=0
    while(j<len(a) and target>=0):
        print(f"target=={target}")
        target-=a[j]
        j+=1
        t+=1
        if target==0:
            c.append(t)

print(c)

