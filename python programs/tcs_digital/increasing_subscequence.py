def solve(n, a):
    a = [0]+a
    for i in range(0, len(a) - 1):
        t = a[i + 1]
        while a[i] < t and a[i] + 1 != t:
            t -= 1
        if t in range(0, a[i + 1] + 1):
            a[i + 1] = t
    if sorted(a[1:]) == a[1:]:
        return ("Yes")
    else:
        return ("No")


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print(out_)