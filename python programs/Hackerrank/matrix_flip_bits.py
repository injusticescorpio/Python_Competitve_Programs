def countFlip(matrix):
    li = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == 0:
                li.append((i, j))
    count = 0
    for i, j in li:
        t = 0
        while (t < len(matrix)):
            if matrix[i][t] == 1:
                matrix[i][t] = -1
                count += 1
            t += 1
        # column conditon
        t = 0
        while (t < len(matrix)):
            if matrix[t][j] == 1:
                matrix[t][j] = -1
                count += 1
            t += 1
    return (count)


test_case = int(input())
for i in range(test_case):
    matrix = []
    m = int(input())
    for i in range(0, m):
        p = list(map(int, input().split(' ')))
        matrix.append(p)
    print(countFlip(matrix))