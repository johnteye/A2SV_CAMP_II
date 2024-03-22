class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @cache
        def dp(r, c):
            if r == n:
                return 0
            if c ==n or c < 0:
                return float("inf")

            return matrix[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1))
        res = float("inf")
    
        for c in range(len(matrix[0])):
            res = min(res, dp(0, c))
    
        return res
