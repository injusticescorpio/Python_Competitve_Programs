li=[(0,0),(0,10),(10,1),(6,4),(6,5),(6,9),(6,1),(6,10),(5,5),(5,6),(1,2),(1,100)]
res=[]
i=0
res1=[]
while i<len(li):
    j=i
    ele=li[i][0]
    p=[]
    while j<len(li) and li[i][0]==li[j][0]:
        p.append(li[j][1])
        j+=1
    for i in sorted(p,reverse=True):
        res1.append((ele,i))
    i=j
print(res1)