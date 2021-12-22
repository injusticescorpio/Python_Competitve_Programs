test_case=int(input())
for i in range(test_case):
    n=int(input())
    a=list(map(int,input().split(' ')))[:n]
    for j in range(1,len(a)+1):
        print(sum(a[0:j]),end=' ')
    print()