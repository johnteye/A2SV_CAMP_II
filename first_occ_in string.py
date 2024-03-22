class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a =31
        m = 10 ** 9 + 7
        def hash(word):
            n = len(word)
            hash_val = 0
            for i in range(n):
                hash_val += a**(n-i-1) *  (ord(word[i]) - ord("a")+ 1)

            return hash_val % m
        
        hash_needle = hash(needle)
        n = len(needle)
        size = haystack[:n]
        hash_size = hash(size)
        if hash_size == hash_needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        for i in range(n, len(haystack)):
            hash_size -=  a**(n-1) * (ord(haystack[i-n]) - ord("a") + 1)
            hash_size *= a
            hash_size += (ord(haystack[i]) - ord("a")+ 1)
            hash_size %= m

            if hash_size == hash_needle:
                return i - n + 1

        return -1

