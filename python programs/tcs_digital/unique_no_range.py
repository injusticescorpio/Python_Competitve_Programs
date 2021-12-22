start,end=list(map(int,input().split(' ')))
for i in range(start,end+1):
    if len(set(str(i)))==len(str(i)):
        print(i,end=' ')
