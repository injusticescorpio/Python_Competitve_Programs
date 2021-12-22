a=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,12,13,15],
    [16,17,17,18,20],
    [21,17,1,1,25]
]

b=[
    [8,9],
    [12,13],
    [17,18]
]
if len(b)>len(b[0]):
    val=len(a)-len(b[0])
else:
    val=len(a)-len(b)
li=[]
flag=0
for  i in range(0,len(a)):
    p=i
    j=0
    k=0
    while j<val:
        print(a[p][j:j+len(b[0])])
        print(li)
        if a[p][j:j+len(b[0])]==b[k]:
            li.append(b[k])
            print(f"li=={li}")
            k+=1
            p+=1
            j-=1
        elif li!=[]:
            li=[]
            k=0
            j=0
            break
        if li==b:
            flag=1
            break
        j+=1
    if flag==1:
        print("True")
        break
