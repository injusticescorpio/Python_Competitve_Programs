def countingValleys(n,k):
    c=0
    p=0
    for i in range(0,len(k)):
        if k[i]=='D':
            c += -1
        elif k[i]=='U':
            c += 1
        if c==0 and k[i]=='U':
            p+=1

    return(p)

n=int(input())
k=input()
print(countingValleys(n,k))