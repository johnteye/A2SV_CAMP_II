class UnionFind:
    def __init__(self, accounts):
        self.root = {}
        self.name = {}

        for account in accounts:
            for i in range(1, len(account)):
                self.root[account[i]] = account[i]
                self.name[account[i]] = account[0]
        

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = UnionFind(accounts)

        for account in accounts:
            for i in range(1, len(account)):
                for j in range(i+1, len(account)):
                    graph.union(account[i], account[j])

        ans = []
        par_chi = defaultdict(list)
        for key in graph.root:
            par_chi[graph.find(key)].append(key)

        for par in par_chi:
            ans.append([graph.name[par]] + sorted(par_chi[par]))
        return ans
        # print(res)

        
        
