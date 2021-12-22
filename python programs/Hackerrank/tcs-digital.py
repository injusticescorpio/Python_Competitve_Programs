def smallest(n):
    if n<10:
        return n+10
    p=[]
    for i in range(9,1,-1):
        while n%i==0:
            n//=i
            p.append(i)
    if n>10:
        return "Not possible"
    else:
        return ''.join(list(map(str,sorted(p))))

n=int(input())
print(smallest(n))
