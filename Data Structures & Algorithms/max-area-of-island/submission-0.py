class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            area = 1
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                area += dfs(i + d[0], j + d[1])
            
            return area

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res