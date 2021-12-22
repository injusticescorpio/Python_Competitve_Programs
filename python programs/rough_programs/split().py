a=input()
b=[]
i=0
while(i<len(a)):
    c=''
    while(i!=len(a) and a[i]!=' '):
        c+=a[i]
        i+=1
    b.append(c)
    i+=1
print(b)