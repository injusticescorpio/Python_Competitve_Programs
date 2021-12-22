from collections import Counter
n=int(input())
li=list(map(int,input().split(' ')))

d=Counter(li)
d1=sorted(d.items(),key=lambda x:x[1])
print(d)