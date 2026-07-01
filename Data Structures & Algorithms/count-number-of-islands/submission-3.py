class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            nonlocal r, c
            if min(i, j) < 0 or i >= r or j >= c or (i, j) in visited or grid[i][j] == '0':
                return 
            
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res


