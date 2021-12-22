a=[5,4,3,2,1,1]

for i in range(0,len(a)):
    pos=i
    for j in range(i+1,len(a)):
        if a[j]<a[pos]:
            pos=j
    if a[pos]<a[i]:
        a[pos],a[i]=a[i],a[pos]
print(f"sorted=={a}")

