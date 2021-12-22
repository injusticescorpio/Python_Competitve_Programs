def largest_num():
    a = list(map(int, input().split(' ')))
    largest = float('-inf')
    for i in a:
        if largest < i:
            largest = i
    c = 0
    for i in a:
        if i == largest:
            c += 1
    print(c)
largest_num()