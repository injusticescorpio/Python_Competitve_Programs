def between_two_sets(a,b):
    li=[]
    for i in range(max(a),min(b)+1):
        li.append(i)
    p=[]
    for i in li:
        c=0
        for j in a:
            if i%j==0:
                c+=1
        if c==len(a):
            p.append(i)
    q=[]
    for i in li:
        c1=0
        for j in b:
            if j% i == 0:
                c1+=1
        if c1==len(b):
            q.append(i)
    z=set(p).intersection(set(q))
    return len(z)









a=[2,4]
b=[16,32,96]
print(between_two_sets(a,b))


#using all

# input();
# a=list(map(int, input().split()))
# b=list(map(int, input().split()))
# ans=0
# for i in range(1, 101):
#     if all(i%x==0 for x in a) and all(x%i==0 for x in b):
#         ans+=1
# print(ans)