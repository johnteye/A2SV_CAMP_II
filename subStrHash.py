class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord('a') + 1
        s = s[::-1]
    
        s_hash, base = 0, 0
        p = 1
        for i in range(k-1):
            s_hash = (s_hash * power) % modulo
            s_hash = (s_hash + val(s[i])) % modulo
            p = (p * power) % modulo
        res = 0
        
        for i in range(k-1, len(s)):
            #add char
            
            s_hash = (s_hash * power) % modulo
            s_hash = (s_hash + val(s[i])) % modulo
        
            if s_hash == hashValue:
                # return s[i-k+1:i]
                res = i
    
            # remove char
            s_hash = (s_hash - p*val(s[i-k+1])) % modulo
    
        ans = s[res - k +1: res+1]
        return ans[::-1]

        
