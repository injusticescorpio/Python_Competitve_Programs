
def counter(d,f):
    c=0
    for i in range(0,len(d)):
        if d[i:i+len(f)]==f:
            c+=1
    return c

a='mmmnm'
stack=['m']
for i in range(1,len(a)):
    if stack[-1][0]==a[i]:
        stack.append(stack[-1]+a[i])
    else:
        stack.append(a[i])
res=0
for i in set(stack):
    res+=counter(a,i)
print(res)



# stack=[['m']]
# def add(stack,a):
#     li=stack[:]
#     li.append(a)
#     return li
# for i in range(1,len(a)):
#     if stack[-1][0]==a[i]:
#         li=add(stack[-1],a[i])
#         stack.append(li[:])
#         print(stack)
#     else:
#         li=[]
#         stack.append([a[i]])
# print(stack)


