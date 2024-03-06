class UnionFind:
    def __init__(self, s1, s2, baseStr):
        arr = set(s1).union(set(s2)).union(set(baseStr))
        self.root = {}
        self.height = {}
        for val in arr:
            self.root[val] = val
            self.height[val] = val

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if U != V:
            if self.root[U] < self.root[V]:
                self.root[V] = U
    
            else:
                self.root[U] = V


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = UnionFind(s1, s2, baseStr)
        n = len(s1)
        ans = ""

        for i in range(n):
            graph.union(s1[i], s2[i])

        for val in baseStr:
            ans += graph.find(val)

        return ans

            
        
