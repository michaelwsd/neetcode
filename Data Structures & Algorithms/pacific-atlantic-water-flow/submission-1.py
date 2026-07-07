class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pacific = [[False] * c for _ in range(r)]
        atlantic = [[False] * c for _ in range(r)]

        def bfs(x, y, m, visited):
            nonlocal r, c
            queue = deque([(x, y)])
            dirc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while queue:
                cx, cy = queue.popleft()
                if (cx, cy) in visited:
                    continue 

                m[cx][cy] = True
                visited.add((cx, cy))
                
                for dx, dy in dirc:
                    newx, newy = cx + dx, cy + dy
                    if (min(newx, newy) < 0 or 
                        newx >= r or 
                        newy >= c or 
                        (newx, newy) in visited or 
                        m[newx][newy] or 
                        heights[newx][newy] < heights[cx][cy]):
                        continue
                    
                    queue.append((newx, newy))

        # fill in pacific 
        for i in range(c):
            if not pacific[0][i]:
                pacific[0][i] = True 
                bfs(0, i, pacific, set())
            
            if not atlantic[r-1][i]:
                atlantic[r-1][i] = True
                bfs(r-1, i, atlantic, set())
        
        for i in range(r):
            if not pacific[i][0]:
                pacific[i][0] = True
                bfs(i, 0, pacific, set())
            
            if not atlantic[i][c-1]:
                atlantic[i][c-1] = True 
                bfs(i, c-1, atlantic, set())

        res = []
        for i in range(r):
            for j in range(c):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res 