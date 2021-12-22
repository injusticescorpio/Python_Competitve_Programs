def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    print(f"indices=={indices}")
    print(f"tup=={tuple(pool[i] for i in indices)}")
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            print(f"i1=={i}")
            if indices[i] != i + n - r:
                print("break")
                break
        else:
            print(f"returning")
            return
        indices[i] += 1
        print(f"indices2=={indices}")
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
            print(f"indices3=={indices}")
        yield tuple(pool[i] for i in indices)

print(list(combinations([1,2,3],2)))