cost=list(map(int,input().split(' ')))
money=int(input())
d = {}
for i in range(0, len(cost)):
    if cost[i] in d:
        # print(i + 1, d[i])
        print(str(d[cost[i]]) + ' ' + str(i+1))
        break
    d[money - cost[i]] = i + 1
    print(d)
