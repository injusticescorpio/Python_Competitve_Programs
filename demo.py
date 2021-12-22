# y=6
# a=[5,1,4,7,3]
# count=a.pop(0)+a.pop(-1)
# print(a)
# k=0
# for i in a:
#    if i>y and k=:
#       count+=y
#    
a=[1,2,3,4,5,6,7,8]
j=0
for i in range(0,len(a)):
    if j==0 or j==1:
        print(a[i])
        j+=1
        continue
    if j==2:
        j=0