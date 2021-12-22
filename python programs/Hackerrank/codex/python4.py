import collections

def tc(n, arr):
    d = collections.defaultdict(list)
    print(arr)
    for i in range(n):
        k,v = arr[i].split()
        if i < n//2:
            d[int(k)].append("-")
        else:
            d[int(k)].append(v)
    print(f"d=={d}")
    od = collections.OrderedDict(sorted(d.items()))
    print(od)
    print(" ".join([" ".join(l) for l in od.values()]))

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
tc(n,arr)