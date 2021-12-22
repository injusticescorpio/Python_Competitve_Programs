def sum_of_digit(n):
    assert n>=0 and int(n)==n,"value must be +ve"
    if n==0:
        return 0
    else:
        return n%10+sum_of_digit(n//10)

print(sum_of_digit(172))

