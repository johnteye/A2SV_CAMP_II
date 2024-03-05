class UnionFind:
    def __init__(self, isConnected):
        self.root = {}
        self.height = {}

        for i in range(isConnected):
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = res = len(isConnected)
        
        graph = UnionFind(n)
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] and graph.find(row) != graph.find(col):
                    res -= 1
                    graph.union(row, col)
        
        return res
        # res = 0
        # for val in graph.root:
        #     if graph.root[val] == val:
        #         res += 1

        # return res

        
