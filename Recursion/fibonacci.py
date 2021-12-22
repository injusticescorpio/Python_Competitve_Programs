def fibo(n):
    assert n>=0 and int(n)==n,"n needs to be positive and no decimal point"
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(5))
