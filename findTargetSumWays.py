class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dp(i, curr_sum):
            # base case
            if i == n:
                if curr_sum == target:
                    return 1
                return 0

            #recurrence relation
            state = (i, curr_sum)
            if state not in memo:
                memo[state] = dp(i+1, nums[i] + curr_sum) + dp(i+1, -(nums[i]) + curr_sum)

            return memo[state]
        memo = {}   
        return dp(0, 0)
