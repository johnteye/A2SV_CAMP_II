class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        def comb(v):
            return (v*(v-1)) / 2

        hashmap = defaultdict(int)
        hashmap[0] = 1
        prefix = 0

        for val in nums:
            prefix += val

            hashmap[prefix % k] += 1
        print(hashmap)
        res = 0
        for val in hashmap.values():
            res += comb(val)

        return int(res)
        
