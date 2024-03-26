class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        base, mod = 31, 10**9 +7

        def val(c):
            return ord(c) - ord("a")
        n, m = len(haystack), len(needle)
        n_hash, m_hash = 0, 0

        for i in range(m):
            m_hash = (m_hash * base) % mod
            m_hash = (m_hash + val(needle[i])) % mod

        p= 1
        for i in range(min(n, m-1)):
            n_hash = (n_hash * base) % mod
            n_hash = (n_hash + val(haystack[i])) % mod
            p = (p* base) % mod

        for i in range(m-1, n):
            # add new char
            n_hash = (n_hash * base) % mod
            n_hash = (n_hash + val(haystack[i])) % mod

            if n_hash == m_hash :
                return i - m + 1


            # remove char
            n_hash = (n_hash - p*val(haystack[i-m+1]))

        return -1



# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         a =31
#         m = 10 ** 9 + 7
#         def hash(word):
#             n = len(word)
#             hash_val = 0
#             for i in range(n):
#                 hash_val += a**(n-i-1) *  (ord(word[i]) - ord("a")+ 1)

#             return hash_val % m
        
#         hash_needle = hash(needle)
#         n = len(needle)
#         size = haystack[:n]
#         hash_size = hash(size)
#         if hash_size == hash_needle:
#             return 0
#         if len(needle) > len(haystack):
#             return -1

#         for i in range(n, len(haystack)):
#             hash_size -=  a**(n-1) * (ord(haystack[i-n]) - ord("a") + 1)
#             hash_size *= a
#             hash_size += (ord(haystack[i]) - ord("a")+ 1)
#             hash_size %= m

#             if hash_size == hash_needle:
#                 return i - n + 1

#         return -1

