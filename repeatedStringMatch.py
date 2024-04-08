class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 0
        N = len(b)
        M = len(a)

        def LPS(string):
            S = len(string)
            lps = [0] * S

            for i in range(1, S):
                j = lps[i - 1]

                while j > 0 and string[i] !=string[j]:
                    j = lps[j - 1]

                if string[i] == string[j]:
                    j += 1

                if j == N:
                    return 1

                lps[i] = j

            return 0

        k = N // M
        for i in range(k, k + 3):
            if LPS(b + "#" + a * i):
                return i
        
        return -1

        
