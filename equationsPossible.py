class UnionFind:
    def __init__(self, parents):
        self.root = {parent:parent for parent in parents}
        

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if self.root[U] < self.root[V]:
                self.root[V] = U
        else:
            self.root[U] = V

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = ""
        for parent in equations:
            parents += parent[0]
            parents += parent[-1]

        parents = set(parents)
        
        graph = UnionFind(parents)
        
        for equation in equations:
            if equation[1] == "=":
                graph.union(equation[0], equation[-1])

        for equation in equations:
                if  equation[1] == "!" and graph.find(equation[0]) == graph.find(equation[-1]):
                    return False

        return True
        
