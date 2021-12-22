def push(data,stack):
    stack.append(data)
    return stack

li=input()
a=[i for i in li]
stack=[]
c=0
p=0
for i in range(0,len(a)):
    print(f'a[i]=={a[i]}')
    print(f"stack=={stack}")
    if (a[i]=='}' or a[i]==')' or a[i]==']') and i==0:
        c=1
        break
    elif (a[i] == '}' or a[i] == ')' or a[i] == ']') and stack == []:
        p=1
        break
    elif a[i]=='{' or a[i]=='(' or a[i]=='[':
        stack=push(a[i],stack)
    elif (a[i]=='}' or a[i]==')' or a[i]==']'):
        print(f"stack[0]=={stack[0]}")
        if stack[-1]+a[i]=='[]' or stack[-1]+a[i]=='{}' or stack[-1]+a[i]=='()':
            stack.pop(-1)
        else:
            break
    else:
        break
print(f"stack=={stack}")
if stack==[] and c==0 and p==0:
    print("yes")
else:
    print("no")






