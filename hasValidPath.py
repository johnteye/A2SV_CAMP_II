class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(y)] = find(x)
        
        R, C = len(grid), len(grid[0])
        right_out = {1, 4, 6}
        left_in = {1, 3, 5}
        down_out = {2, 3, 4}
        up_in = {2, 5, 6}
        
        for i in range(R):
            for j in range(C):
                # Connect left and right
                if j > 0 and grid[i][j-1] in right_out and grid[i][j] in left_in:
                    union((i, j-1), (i, j))
                # Connect up and down
                if i > 0 and grid[i-1][j] in down_out and grid[i][j] in up_in:
                    union((i-1, j), (i, j))
        
        return find((0, 0)) == find((R-1, C-1))
