a=input()
b=input()
i=j=c=k=0
while(i<len(a)):
    for j in range(0,len(b)):
        if a[i+j]==b[j]:
            c+=1
        else:
            c=0
            break
    if c==len(b):
        k+=1
        c=0
    i+=1
print(k)

