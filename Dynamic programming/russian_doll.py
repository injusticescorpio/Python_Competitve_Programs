#In russianDoll doll make the width in ascending order and height in descending order(for same key value) then perform LIS on height
li=[(5,4),(6,4),(6,7),(2,3)]
li=sorted(li,key=lambda x:x[0])
i=0
res=[]
while i<len(li):
    j=i
    p=[]
    while j<len(li) and li[j][0]==li[i][0]:
        p.append(li[j][1])
        j+=1
    for k in sorted(p,reverse=True):
        res.append((li[i][0],k))
    i=j
print(res)

lis=[]
# extract the part for LIS
for i in res:
    lis.append(i[1])
print(lis)

#LIS