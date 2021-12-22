def check_beautiful(n):
    li=tuple(int(i) for i in str(n))
    d={}
    for i in li:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i,j in d.items():
        if i!=j:
            return False
    return True



def beautifulNumber (N):
    for i in range(N+1,10**12+1):
        if check_beautiful(i):
            return i

T = int(input())
for _ in range(T):
    N = int(input())

    out_ = beautifulNumber(N)
    print (out_)