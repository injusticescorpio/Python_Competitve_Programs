n=int(input())
a=list(map(int,input().split(' ')))
#0 0 1 0 0 1 0
c=0
i=0
while(i<len(a)):
    print(f"i=={i}")
    if i+2<len(a) and a[i+2]==0:
        c+=1
        i+=2
    elif i+1<len(a) and a[i+1]==0:
        c+=1
        i+=1
    else:
        break
print(c)