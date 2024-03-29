# shortest path algorithm, basically bfs with heaps instead of a queue

import heapq
heap = []
heapq.heapify(heap)
visited = set()

def bfs(src, dest):
    heapq.heappush(heap, (0, src))
    visited.add(src)

    while heap:
        curr = heapq.heappop(heap)
        visited.add(curr[1])
        
        if curr[1] == dest:
            return curr[0]
            
        for neighbour in graph[curr[1]]:
            if neighbour[0] not in visited:
                heapq.heappush(heap, (curr[0] + neighbour[1], neighbour[0]))




edges = [["A", "B", 9], ["A", "B", 10], ["A", "C", 3], ["C", "B", 1], ["C", "B", 5] ]

graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))


print(bfs("A", "B"))





        
