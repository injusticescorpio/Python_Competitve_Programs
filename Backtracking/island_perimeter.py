def main():
    grid=[[1,1,1],[1,0,0],[0,0,0]]
    path = set()
    res = []
    def dfs(i, j):

        if (i, j) in path:
            return 0
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) or grid[i][j] == 0:
            res.append(1)
            return
        path.add((i, j))
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        # path.remove((i, j))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                print(i,j)
                dfs(i, j)
                print(sum(res))
                print(path)
                return
main()
