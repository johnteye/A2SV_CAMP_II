class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
    
        nums.sort()
        min_diff = float('inf')
        
        for i in range(4):
            diff = nums[-4 + i] - nums[i]
            min_diff = min(min_diff, diff)
        
        return min_diff

        
