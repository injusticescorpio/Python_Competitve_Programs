count = [0]*6
for t in map(int,input().split(' ')):
    count[t] += 1
print(count)
print(count.index(max(count)))