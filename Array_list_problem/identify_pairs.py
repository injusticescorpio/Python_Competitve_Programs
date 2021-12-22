# a=[int(i) for i in input().split(' ')]
# b=[int(i) for i in input().split(' ')]
a=[9,2,4,14,5,1,3]
b=[1,12,7,9,2,3]
pairs=[]
if a is None or b is None:
    print(-1)
    exit()
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]%2==0 and b[j]%2==0:
            if sum(a)==sum(b):
                pairs.append((a[i],b[j]))
                continue
            else:
                x = a[:]
                y = b[:]
                x[i],y[j] = y[j], x[i]
            if sum(x) == sum(y):
                pairs.append((x[i], y[j]))
                continue
        elif a[i]%2!=0 and a[i]%2!=0:
            if sum(a)==sum(b):
                pairs.append((a[i],b[j]))
                continue
            else:
                x=a[:]
                y=b[:]
                x[i],y[j]=y[j],x[i]
            if sum(x)==sum(y):
                pairs.append((x[i],y[j]))
                continue
        else:
            pass

for i in pairs:
    if i[0]*i[1]%2==0:
        print(f"{i[1]},{i[0]},",end='')
for i in pairs:
    if i[0]*i[1]%2!=0:
        print(f"{i[1]},{i[0]},",end='')