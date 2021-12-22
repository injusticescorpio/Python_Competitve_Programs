def power(x,n):
    print(f"x=={x} and n=={n}")
    assert n>=0 and int(n)==n,"value must be +ve"
    if n==0:
        return 1
    else:
        return x*power(x,n-1)


print(pow(0,0))
