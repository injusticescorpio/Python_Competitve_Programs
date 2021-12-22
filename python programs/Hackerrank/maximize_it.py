from itertools import product
# print(list(product((1,2,3),(4,5,6),(7,8,9))))
k,m=map(int,input('').split(' '))
li=[tuple(map(int,input('').split(' '))) for i in range(k)]
l=[]
for i in product(*li):
    l.append((sum([j**2 for j in i])%m))
print(l)

