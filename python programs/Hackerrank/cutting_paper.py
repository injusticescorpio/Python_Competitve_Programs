

def paper(m,n):
    if (m==n):
        return (m**2)-1
    else:
        return min(m,n)*(max(m,n)-1)
m,n=list(map(int,input().split(' ')))
print(paper(m,n))