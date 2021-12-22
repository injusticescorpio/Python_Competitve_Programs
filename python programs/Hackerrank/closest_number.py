a=list(map(int,input().split(' ')))
li=sorted(a)
small=float('inf')
res=[]
for i in range(0,len(li)-1):
    if (li[i+1]-li[i])<small:
        small=li[i+1]-li[i]
for i in range(0,len(li)-1):
    if (li[i+1]-li[i])==small:
        res.append(li[i])
        res.append(li[i+1])
print(res)
    
