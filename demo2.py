friends=int(input())
time=int(input())
a=[i for i in range(1,friends+1)]
stack=a[:]
greater=max(a)
less=min(a)

while len(stack)<time:
    if stack[-1]==greater:
        k=1
        while k!=len(a):
            stack.append(stack[-1]-1)
            k+=1
    elif stack[-1]==less:
        k=1
        while k!=len(a):
            stack.append(stack[-1]+1)
            k+=1
print(stack[time-1],stack[time])
