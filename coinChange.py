# top to down approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(amount):
            #base case
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]

            # recurrence relation
            res = float("inf")
            for coin in coins:
                res = min(res, dp(amount-coin) + 1)
            memo[amount] = res
            return res

        memo = {}
        res = dp(amount)
        if res >= float("inf"):
            return -1
        return dp(amount)

# bottom up approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1) 
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
    
        return dp[amount] if dp[amount] != float("inf") else -1

      
