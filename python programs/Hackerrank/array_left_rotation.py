n,d=[int(i) for i in input().split(' ')]
a=[int(i) for i in input().split(' ')][:n]
# for i in range(d):
#     a=a[1:]+[a[0]]
# print(a)
# for i in range(d):
#     t=a[0]
#     for j in range(1,len(a)):
#         a[j-1]=a[j]
#     a[len(a)-1]=t
# print(*a)
for i in range(d):
    a.append(a.pop(0))
print(a)