from collections import Counter
n=int(input())
a=list(map(int,input().split(' ')))
counter=Counter(a)
l=[]
for i in counter.items():
    l.append(i[1]//2)
print(sum(l))
