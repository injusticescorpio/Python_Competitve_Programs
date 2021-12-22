a=[
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
li=[]
for i in range(len(a)):
    k=[]
    for j in range(len(a)):
        k.append(a[j][i])
    li.append(tuple(k))
        

print(li)