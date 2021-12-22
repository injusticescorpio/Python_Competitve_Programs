def countSort(arr):
    print(arr)
    res=[[] for _ in range(0,len(arr))]
    mid=len(arr)//2
    for i in range(0,len(arr)):
        if i<mid:
            res[int(arr[i][0])].append('-')
        else:
            res[int(arr[i][0])].append(arr[i][1])
    for i in res:
        if i:
            print(*i,end=' ')




if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)