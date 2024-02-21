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
