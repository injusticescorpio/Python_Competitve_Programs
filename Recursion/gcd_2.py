def gcd(a,b):
    print(f"a=={a} and b=={b}")
    if a==0:
        return b
    return gcd(b%a,a)

print(gcd(25,60))