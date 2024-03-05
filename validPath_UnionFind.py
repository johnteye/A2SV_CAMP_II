class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.height = {}

        for i in range(n):
            self.root[i] = i
            self.height[i] = 1

    def find(self, x):
        if x == self.root[x]:
            return x

        return self.find(self.root[x])
    

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if U != V:
            if self.height[U] > self.height[U]:
                self.root[V] = U
                self.height[U] += self.height[V]
            else:
                self.root[U] = V
                self.height[V] += self.height[U]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = UnionFind(n)

        for u , v in edges: graph.union(u, v)

        return graph.find(source) == graph.find(destination)
        
