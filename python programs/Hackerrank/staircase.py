def staircase(n,i):
    # Write your code here
    if n==0:
        return
    print(' '*(n-1),end='')
    print('#'*i)
    staircase(n-1,i+1)
staircase(4,1)
