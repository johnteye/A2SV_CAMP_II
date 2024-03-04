class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        hold, not_hold = [0] * n, [0] * n
        hold[0] = -prices[0] - fee
        
        for i in range(1, n):

            hold[i] = max(hold[i-1], not_hold[i-1] - prices[i] - fee)

            not_hold[i] = max(not_hold[i-1], hold[i-1] + prices[i])
        
        return not_hold[-1]
        
