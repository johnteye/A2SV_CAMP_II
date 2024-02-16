class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ (n >> 1)
        return n.bit_count() == n.bit_length()
