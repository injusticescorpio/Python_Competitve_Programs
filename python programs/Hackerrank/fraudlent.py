def median(li):
    n=len(a)
    if n%2==0:
        median=(a[n//2]+a[(n//2)-1])/2
        return median
    else:
        return a[n//2]

notice=0
n,d=list(map(int,input().split(' ')))
a=[int(i) for i in input().split(' ')][:n]
a=sorted(a)
for i in range(n-d):
    print(a[i:d+i])
    if a[d+i]>=2*median(a[i:d+i]):
        notice+=1
print(f"notice=={notice}")






