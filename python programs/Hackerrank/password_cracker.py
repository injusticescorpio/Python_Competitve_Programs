
a={}
def password_generator(password,login):
    print(f"login=={login}")
    global a
    print(f"a=={a}")
    if len(login)==0:
        return True,[]
    if login in a:
        print("executed")
        return False,[]
    for i in password:
        if login.startswith(i):
            a[login] = True
            valid,result =password_generator(password,login[len(i):])
            print(f"valid=={valid}")
            if valid:
                return True,[i]+result
    return False,[]

def password_cracker(password,login):
    global a
    a={}
    valid,result1=password_generator(password,login)
    if valid:
        return ' '.join(result1)
    else:
        return 'WRONG PASSWORD'




password=tuple(input(' ').split(' '))
login=input()
print(password_cracker(password,login))

