cost=list(map(int,input().split(' ')))
money=int(input())
saved = {}
for i, n in enumerate(cost):
    if money - n in saved:
        print(saved[money - n], i + 1)
    saved[n] = i + 1