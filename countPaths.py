class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        heap = []
        heapq.heapify(heap)
        visited = set()
        
        
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((t, v))
            graph[v].append((t, u))

        heapq.heappush(heap, (0, 0))
        min_dist = [0] * n

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            
            
            min_dist[node] = cost            
               
            for time, neigh in graph[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (cost+time, neigh))
        # print(min_dist)
    
        def dp(node, c):
            if node in memo:
                return memo[node]

            if c == min_dist[-1]:
                return 1
            cum_sum = 0
            for time, neigh in graph[node]:
                if time + c + min_dist[neigh] == min_dist[-1]:
                    cum_sum += dp(neigh, c + time)%(10**9+7)
            memo[node] = cum_sum
            return memo[node]
        memo ={}
        return dp(n-1, 0) %(10**9 + 7)
