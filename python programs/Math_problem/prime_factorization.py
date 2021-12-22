n=int(input('Enter a number'))
i=2
while(i*i<=n):
    count=0
    if n%i==0:
        while(n%i==0):
            count+=1
            n=n//i
        print(i,'^',count)
    i+=1
if n>1:
    print(n,'^',1)

