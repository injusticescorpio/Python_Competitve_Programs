nums=list(map(int,input().split(',')))
print(nums)
p=[]
n=[]
for i in nums:
    if i<0:
        n.append(i)
    else:
        p.append(i)
print(f"n=={n}")
print(f"p=={p}")
res=[]
for i in range(0,len(p)):
    for j in range(i+1,len(p)):
        if -1*(p[i]+p[j]) in n:
            res.append([p[i]]+[p[j]]+[-(p[i]+p[j])])

for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if -1*(n[i]+n[j]) in p:
            res.append([n[i]]+[n[j]]+[-1*(n[i]+n[j])])
print(res)
res1=list(set(map(lambda i:tuple(sorted(i)),res)))
