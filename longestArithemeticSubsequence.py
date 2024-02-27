class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = defaultdict(int)
        for val in arr:
            if (val - difference) in hashmap:
                hashmap[val] = hashmap[val - difference] + 1

            else:
                hashmap[val] = 1

     
        return max(hashmap.values())
