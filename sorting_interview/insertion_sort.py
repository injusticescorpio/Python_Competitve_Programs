a=[5,4,3,2,1,1]

for i in range(1,len(a)):
    j=i-1
    key=a[i]
    while(j>=0 and a[j]>key):
        a[j+1]=a[j]
        j-=1
    a[j+1]=key



print(f"sorted=={a}")