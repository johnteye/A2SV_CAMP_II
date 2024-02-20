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
