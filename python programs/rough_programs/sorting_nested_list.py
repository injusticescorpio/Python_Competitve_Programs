#input:
a=[[1,0,-1],[-1,1,0],[1,3],[3,1],[-1,-1,2],[0,1,-1]]
#output
# a=[[1,0,-1],[1,3],[-1,-1,2]]

# a=list(set(tuple(sorted(i)) for i in a))
# print(a)
# #or
# res1=list(set(map(lambda i:tuple(sorted(i)),a)))
# print(res1)
# #or
set=[]
for i in a:
    if sorted(i) not in set:
        set.append(sorted(i))
print(set)
