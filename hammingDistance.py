class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y

        return res.bit_count()       
