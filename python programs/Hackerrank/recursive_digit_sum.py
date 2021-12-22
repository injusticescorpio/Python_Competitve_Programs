def sum_of_numbers(st):
    s = 0
    a=int(st)
    while (a > 0):
        d = a % 10
        s += d
        a //= 10
    return s

def recursiveDigitSum(p):
    print(f"p=={p}")
    if int(p)<=9:
        return p
    else:
        y=str(sum_of_numbers(p))
        return recursiveDigitSum(y)

n,k=list(map(int,input('').split(' ')))
l=sum_of_numbers(n)*k
recursiveDigitSum(l)

