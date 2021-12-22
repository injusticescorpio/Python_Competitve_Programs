def path_finding(N,arr):
    if N<2:
        return 'Invalid Input'
    if sum(arr)==arr[0]*N:
        return 'Equal'
    smallest_no=float('inf')
    for i in arr:
        if smallest_no>i:
            smallest_no=i
    print(smallest_no)
    for i in arr:
        if smallest_no1>i and i!=smallest_no:
            smallest_no1=i
    print(smallest_no1)

N=int(input())
arr=[]
for i in range(N):
    k=int(input())
    arr.append(k)
path_finding(N,arr)
