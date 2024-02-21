class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)
        def dp(i, target_sum):
            #base case
            if i >= n or target_sum <= 0:
                return target_sum == 0

            # recurrence relation
            if (i, target_sum) not in memo:
                memo[(i, target_sum)] = dp(i+1, target_sum - nums[i]) or dp(i+1 , target_sum)

            
            return memo[(i, target_sum)]

        return sum(nums) % 2 == 0 and dp(0, sum(nums)//2)
