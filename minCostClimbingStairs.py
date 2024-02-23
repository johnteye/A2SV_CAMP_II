class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(i):
            if i >= len(cost):
                return 0
            if i not in memo:
                one, two = dp(i+1), dp(i+2)
                memo[i] = cost[i] + min(one, two)

            return memo[i]

        memo = {}
        return min(dp(0), dp(1))

# bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0,0]
     
        
        for i in range(2, n +  1):
            temp = dp[1]
            dp[1] = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[0]= temp
        
        return dp[1]
