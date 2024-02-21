class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [0]* (n + 1)
        if n >= 2 :
            memo[1] = 1
        else:
            return n
        
        def dp(i):
            if i < 2:
                return i
            if i % 2 == 0:
                idx = i // 2
                memo[i] = dp(idx)

            else:
                idx = i // 2
                memo[i] = dp(idx) + dp(idx+1)

            return memo[i]


        for i in range(2, n+1):
            res = max(0,dp(i))
        
        return max(memo)
