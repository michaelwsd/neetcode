class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        INF = 2 ** 31 - 1

        def bfs(i, j):
            queue = deque([[i, j, 0]])
            visited = [[0] * c for _ in range(r)]
            dist = float('inf')

            while (len(queue) > 0):
                x, y, steps = queue.popleft()

                if grid[x][y] == 0: return min(dist, steps)
                visited[x][y] = True

                for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    newX, newY = x + d[0], y + d[1]
                    if newX < 0 or newX >= r or newY < 0 or newY >= c or visited[newX][newY]:
                        continue
                    if grid[newX][newY] == -1: continue
                    if  INF > grid[newX][newY] > 0: 
                        dist = min(dist, grid[newX][newY] + steps + 1)
                        continue
                    queue.append([newX, newY, steps+1])
            

            return -1 if dist == float('inf') else dist

        for i in range(r):
            for j in range(c):
                if grid[i][j] > 0:
                    steps = bfs(i, j)
                    if steps != -1:
                        grid[i][j] = bfs(i, j)
        