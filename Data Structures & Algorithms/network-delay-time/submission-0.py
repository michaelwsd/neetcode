class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))
            
        heap = [(0, k-1)]

        dist = [float('inf')] * n
        visited = [False] * n
        dist[k-1] = 0

        while heap:
            time, node = heapq.heappop(heap)

            if visited[node]: continue
            visited[node] = True 

            for nei, w in graph[node]:
                if visited[nei]: continue 
                if dist[node] + w < dist[nei]:
                    dist[nei] = dist[node] + w
                    heapq.heappush(heap, (dist[node] + w, nei))
        
        res = max(dist)
        return res if res != float('inf') else -1 
