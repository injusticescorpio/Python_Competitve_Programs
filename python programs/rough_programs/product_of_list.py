def product(a,i,subset=[],res=[]):
    if i>=len(a):
        pass
    for j in range(len(a[i])):
        subset.append(a[i][j])
    product(i+1)






a=[[1,2],[3,4]]
for i in a[0]:
    product(a,i,1)