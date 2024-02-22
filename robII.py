class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return  0
        if len(nums) ==  1:
            return nums[0]

        def rob_range(start, end):
            memo = {}
            def dp(i):
                if i in memo:
                    return memo[i]
                if i >= end:
                    return  0
                rob, not_rob = nums[i] + dp(i +  2), dp(i +  1)
                memo[i] = max(rob, not_rob)
                return memo[i]
            return dp(start)
            
        return max(rob_range(0, len(nums) -  1), rob_range(1, len(nums)))
