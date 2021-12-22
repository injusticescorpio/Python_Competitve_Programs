def findSum(numbers, queries):
    p = []
    numbers = [None] + numbers
    for i in queries:
        l, r, x = i
        res = []
        for i in range(l, r + 1):
            res.append(numbers[i])
        print(res)
        for i in range(0, len(res)):
            if res[i] == 0:
                res[i] = x
        print(f"new r=={res}")
        p.append(sum(res))


    return p

numbers=[-5,0]
queries=[[2,2,20],[1,2,10]]
print(findSum(numbers,queries))