a=[int(i) for i in input().split(' ')]
# # Insertion sort 1 with python
# for i in range(1,len(a)):
#     print(a)
#     x=a[i]
#     j=i-1
#     while(j>=0 and a[j]>x):
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=x
print(a)
# Insertion sort 2 with python 2
for i in range(1,len(a)):
    print(a)
    x=a[i]
    for j in range(i-1,-2,-1):
        if a[j]>x:
            a[j+1]=a[j]
        else:
            break
    a[j+1]=x
print(a)