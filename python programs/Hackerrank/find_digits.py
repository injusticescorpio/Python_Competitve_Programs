def findDigits(n):
    # Write your code here
    c=0
    k=n
    while(n>0):
        d=n%10
        # print(f"d=={d}")
        # if d==0:
        #     return 1
        if d!=0 and k%d==0:
            c+=1
        n=n//10
    return c
print(findDigits(10))