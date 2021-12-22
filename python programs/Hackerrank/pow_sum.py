import sys
sys.setrecursionlimit(10**9)
def pow_sum(arr,n,p):
    print(f"arr=={arr} n=={n}")
    if arr==[] and n==0:
        return 1
    if arr==[]:
        return 0
    ways=pow_sum(arr[1:],n,p)+pow_sum(arr[1:],n-(arr[0]**p),p)
    return ways

n=int(input())
p=int(input())
arr=[]
for i in range(1,int(n**(1/p))+1):
    arr.append(i)
print(pow_sum(arr,n,p))