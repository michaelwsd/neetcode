class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(i, j, sea_type, prev):
            if (min(i, j) < 0 or i >= r or j >= c 
                or ((i, j) in sea_type) 
                or heights[i][j] < prev):
                return
            
            sea_type.add((i, j))
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(i+d[0], j+d[1], sea_type, heights[i][j])
        
        # start from the borders, use dfs to add all reachable cells to the sets
        # horizontal
        for i in range(c):
            dfs(0, i, pac, heights[0][i])
            dfs(r-1, i, atl, heights[r-1][i])

        # vertical 
        for i in range(r):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, c-1, atl, heights[i][c-1])

        res = []
        for i in range(r):
            for j in range(c):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
