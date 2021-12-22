def bank_account(amount,account):
    if float(amount)>=float(account):
        return account
    else:
        if amount%5==0:
            account-=(amount+0.50)
            return account
        else:
            return account

def fun(i):
    k=float(i)
    p=round(k,2)
    return p

amount,account=list(map(fun,input('').split(' ')))
# print(amount)
print ("{0:.2f}".format(bank_account(amount,account)))


