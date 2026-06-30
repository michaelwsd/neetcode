class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        heap = [] # dist, x, y
        r, c = len(grid), len(grid[0])
        visited = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    heapq.heappush(heap, [0, i, j])
        
        while heap:

            dist, x, y = heapq.heappop(heap)

            if (x, y) in visited: continue
            visited.add((x, y))
            grid[x][y] = dist

            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                newX, newY = x + d[0], y + d[1]
                if min(newX, newY) < 0 or newX == r or newY == c or (newX, newY) in visited or grid[newX][newY] == -1:
                    continue
                
                heapq.heappush(heap, [dist+1, newX, newY])


