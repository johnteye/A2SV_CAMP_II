class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perm = ''
        res = []
        def backtrack(perm, seen):
            if len(perm) == n:
                res.append(perm.copy())
                return 
            if len(res)== k:
                return 

            for i in range(1, n+1):
                if i not in seen:
                    perm.append(i)
                    seen.add(i)
                    backtrack(perm, seen)
                    perm.pop()
                    seen.remove(i)

        backtrack([], set())
        return "".join(map(str, res[-1]))

        # res = list(permutations([i+1 for i in range(n)]))
        # ans = ""
        # for val in res[k-1]:
        #     ans += str(val)

        # return ans
        
