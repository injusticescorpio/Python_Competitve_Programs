
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def solve(n, r):
    return (fact(n)//(fact(n-r)*fact(r)))%14287

# print(fact(5))
print(solve(1900000,10000))
