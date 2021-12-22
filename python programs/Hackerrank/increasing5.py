n=int(input())
a=list(map(int,input().split(' ')))[:n]
c=0
for i in range(1,len(a)):
    if a[i-1]>a[i]:
        c+=a[i-1]-a[i]
        a[i]=a[i-1]
print(c)

