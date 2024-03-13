class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dijkstra's algorithm
        graph = defaultdict(list)
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))
        

        heap = []
        heapq.heapify(heap)
        visited = set()
        check = set()
        for i in range(n):
            check.add(i+1)
        
        def bfs(src):
            heapq.heappush(heap, (0, src))
            visited.add(src)

            while heap:
                curr = heapq.heappop(heap)
                visited.add(curr[1])
                
                if visited == check:
                    return curr[0]

                
                for neighbour in graph[curr[1]]:
                    if neighbour[0] not in visited:
                        heapq.heappush(heap, (curr[0] + neighbour[1], neighbour[0]))
            return -1
    
        return bfs(k)

    

        #floyd- warshall algorithm 
        dp = [[float("inf")]*n for _ in range(n)]

        for u, v, w in times:
            dp[u-1][v-1] = w

        for i in range(n):
            dp[i][i] = 0

        for alt in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][alt] + dp[alt][j])
     
 
        return max(dp[k-1]) if max(dp[k-1]) != float("inf") else -1

        
