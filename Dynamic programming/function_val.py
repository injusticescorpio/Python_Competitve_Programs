from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations(['1','2','2','3','3','3'])
li=[int(''.join(i)) for i in list(perm)]
perm1= permutations(['1','2','2','3','3','3','4','4','4','4'])
li1=[int(''.join(i)) for i in list(perm1)]
res=li+li1
p=sorted(res)
