a=[
[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0],
]
s=0
p=[]
for i in range(0,len(a)-2):
    l=[]
    for j in range(i,3+i):

        for k in range(i,3+i):
            # if j==k==(3+2*i)//2:
            #     s+=a[j][k]
            #     continue
            # else:
            #     s+=a[j][k]
            l.append(a[j][k])
        p.append(l)
print(p)






