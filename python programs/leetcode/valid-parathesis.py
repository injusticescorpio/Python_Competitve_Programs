#(()()()())
s=input()
stack=[]
m=0
stack.append(-1)
for i in range(0,len(s)):
    if s[i]=='(':
        stack.append(i)
    else:
        stack.pop()
        if stack==[]:
            stack.append(i)
        else:
            l=i-stack[-1]
            m=max(m,l)
        l=i-stack[-1]
        m=max(m,l)
    print(stack)
print(m)
