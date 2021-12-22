def fun(a,b,k):
    p=0
    if a==b and k==0 or a==b and 2*len(a)==k or a==b and 2*len(a)+1==k:
        return 'Yes'
    while (p < min(len(a), len(b)) and a[p] == b[p]):
        p += 1
    q=len(a[p:len(a)])+len(b[p:len(b)])

    if (q==k or k%(2*q+1)==0) or  (len(a)>1 and a[-1]==b[0] and k%(len(a)-1)==0):
        return 'Yes'
    x=p+1
    for i in range(1,x+1):
        if q+2*i==k:
            return 'Yes'
    return 'No'










a=list(input())
b=list(input())
k=int(input())
p=0
print(fun(a,b,k))






