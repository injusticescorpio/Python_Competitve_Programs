# d={1:2,3:10,9:5,-1:-2}
# print(sorted(d.items(),key=lambda _:_[1],reverse=True))
from collections import  Counter
a=list(map(int,input().split(' ')))
k=sorted(Counter(a).items(),key=lambda _:_[1],reverse=True)
highest=k[0][1]
minimum=k[0][0]
i=1
while(i<len(k) and k[i][1]==highest):
    if minimum>k[i][0]:
        minimum=k[i][0]
    i+=1
print(minimum)