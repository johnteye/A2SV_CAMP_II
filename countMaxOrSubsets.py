class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def bit_or(arr):
            res = 0
            for val in arr:
                res |= val
            return res

        target, count, n = bit_or(nums), 0, len(nums)


        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if (i & (1 << j)) > 0] 
            if bit_or(subset) == target:
                count += 1

        return count
