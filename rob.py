class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(i):
            if i >= len(nums):
                return 0

            if i not in memo:
                rob, not_rob = nums[i] + dp(i+ 2), dp(i + 1)
                memo[i] = max(rob, not_rob)

            return memo[i]

        memo = {}
        return dp(0)


        
