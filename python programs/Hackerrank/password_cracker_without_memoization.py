
def password_generator(password,login):
    print(f"login=={login}")
    if len(login)==0:
        return True,[]
    for i in password:
        if login.startswith(i):
            valid,result =password_generator(password,login[len(i):])
            print(f"valid=={valid}")
            if valid:
                return True,[i]+result
    return False,[]

def password_cracker(password,login):
    valid,result1=password_generator(password,login)
    if valid:
        return ' '.join(result1)
    else:
        return 'WRONG PASSWORD'

#here the problem is that on running this
#with inputs
# a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa
#aaaaaaaaaab
# after completing all operations,login=b
#it backtracks and calls the function one more time
#so inorder to avoid that we will use memoization.


password=tuple(input(' ').split(' '))
login=input()
print(password_cracker(password,login))

