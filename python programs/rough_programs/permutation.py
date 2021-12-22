from itertools import combinations

# Get all permutations of [1, 2, 3]
# perm = combinations([1, 2],1)
# c=0
# for i in perm:
#     c+=1
# print(c)
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)
