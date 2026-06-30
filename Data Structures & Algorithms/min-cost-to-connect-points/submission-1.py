class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)

        for i in range(len(points)):
            u1, v1 = points[i]
            for j in range(i+1, len(points)):
                u2, v2 = points[j]
                dist = abs(u2 - u1) + abs(v2 - v1)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        res = 0
        visited = set()
        # start from arbitrary point
        minH = [[0, 0]] # cost, point
        while len(visited) < n:
            cost, point = heapq.heappop(minH)

            if point in visited: continue
            res += cost
            visited.add(point)

            for neiCost, nei in graph[point]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return res




