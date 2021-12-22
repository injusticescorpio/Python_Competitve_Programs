from collections import Counter
n=int(input())
a=list(map(int,input().split(' ')))
c=sorted(Counter(a).items(),key=lambda x:x[1],reverse=True)
print(n-c[0][1])
