n=int(input())
l=[int(i) for i in input().split()]
maximum=0
for i in l:
    c=l.count(i)
    print(f"i=={i} and count=={c}")
    d=l.count(i-1)
    print(f"i-1=={i-1} and count={d}")
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)