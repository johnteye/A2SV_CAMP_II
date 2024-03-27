class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0]* (n + 2)

        def new(c, e):
            res = ord(c) - ord("a")
            res = (res + e) % 26
            return chr(res + ord("a"))


        for l, r, val in shifts:
            if val == 0:
                diff[l+1] -= 1
                diff[r+2] += 1
            else:
                diff[l+1] += val
                diff[r+2] -= val

        prefix = [0]
        for val in diff:
            prefix.append(prefix[-1] + val)

    
        prefix = prefix[2:]
        ans = list(map(str, s.strip()))

    
        for i in range(n):
            ans[i] = new(s[i], prefix[i])
        return "".join(ans)
        
