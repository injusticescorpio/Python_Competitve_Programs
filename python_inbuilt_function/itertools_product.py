def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    print(pools)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    print(result)
    for prod in result:
        yield tuple(prod)

print(list(product([1,2,3],[3,4])))