def birthday(s, d, m):
    k=0
    for i in range(0,len(s)-m+1):
        p=0
        for j in range(i,i+m):
            p+=s[j]
        if p==d:
            k+=1
    return k

print(birthday([1,1,1,1,1,1],3,2))
