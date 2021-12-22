def gcd(a,b):
    print("a==",a,"b==",b)
    assert int(a)==a and int(b)==b,"Number must be integer"
    a=abs(a)
    b=abs(b)
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(0,0))


