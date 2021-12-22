n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
h=0
for i in N:
    if i in A:
        h+=1
for j in N:
    if j in B:
        h-=1
print(h)