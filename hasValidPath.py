class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        unionfind = {}
        def find(x):
            unionfind.setdefault(x,x)
            if x == unionfind[x]:
                return x
            unionfind[x] = find(unionfind[x])
            return unionfind[x]

        def union(x, y):
            unionfind[find(y)] = find(x)

        left_in = {1, 3, 5}
        right_out = {1, 4, 6}
        down_out = {2, 3, 4}
        up_in = {2,5,6}

        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                
                if j > 0 and grid[i][j - 1] in right_out and grid[i][j] in left_in:
                    union((i, j - 1), (i, j))

                if i > 0 and grid[i - 1][j] in down_out and grid[i][j] in up_in:
                    union((i -1 , j), (i, j))

        return find((0, 0)) == find((row-1, col-1))
