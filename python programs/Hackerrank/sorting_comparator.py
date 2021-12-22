n=int(input())
li=list(tuple(map(lambda x: int(x) if x[0] in '0123456789' else x, input().split(' '))) for i in range(n))
print(li)
li=sorted(li,key=lambda x:x[1],reverse=True)
i=j=0
final=[]
print(li)
while(i<len(li)):
    p=[]
    while(j<len(li) and li[j][1]==li[i][1]):
        p.append(li[j])
        j+=1
    print(p)
    for k in sorted(p,key=lambda x:x[0]):
        final.append(k)
    i=j
print(final)

