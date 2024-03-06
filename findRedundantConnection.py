class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.size = {}

        for i in range(n):
            self.root[i+1] = i + 1
            self.size[i+1] = 1

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if U != V:
            if self.size[U] > self.size[V]:
                self.root[V] = U
                self.size[U] += self.size[V]

            else:
                self.root[U] = V
                self.size[V] += self.size[U]

        else:
            return [u, v]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = UnionFind(n)

        for u , v in edges:
            res = graph.union(u, v)
            if res:
                return res
