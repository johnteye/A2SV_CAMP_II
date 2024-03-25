class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        n = len(nums)
        if not target: return 0

        hashmap = {0:-1}
        prefix = []
        count=0
        for num in nums:
            count+=num
            prefix.append(count)
        
        min_cost =n
        
        for i in range(n):
            curr = prefix[i]%p
            hashmap[curr] = i

            if (curr - target)%p in hashmap:
                min_cost = min(min_cost, i- hashmap[(curr - target)%p])
                
            
        return min_cost if min_cost!=n else -1
