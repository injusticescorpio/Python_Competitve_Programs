# 64 25 12 22 11
a=[int(i) for i in input().split(' ')]
for i in range(0,len(a)):
    print(a)
    pos=i
    for j in range(i+1,len(a)):
        if a[pos]>a[j]:
            pos=j
    if a[i]>a[pos]:
        a[i],a[pos]=a[pos],a[i]
print(a)