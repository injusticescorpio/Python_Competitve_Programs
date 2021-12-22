n=int(input())
c=0
r=0
if n<0:
    n=n*-1
    c=1
while(n>0):
    d=n%10
    r=(r*10)+d
    n//=10
if r not in range(-2**31,(2**31)-1):
    print(0)
elif c==1:
    print(-r)
else:
    print(r)
