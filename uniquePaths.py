class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(row, col):
            return 0 <= col < n and 0 <= row < m
        
        def dp(row, col):
            #base case
            if (row, col) == (m-1, n-1):
                return 1
            
            if not inbound(row, col):
                return 0
            
            #recurrence relation

            if (row, col) not in memo:
                down = dp(row+1, col)
                right = dp(row, col+1)
                memo[(row, col)] = down + right

            return memo[(row, col)]
        memo = {}
        return dp(0, 0)
