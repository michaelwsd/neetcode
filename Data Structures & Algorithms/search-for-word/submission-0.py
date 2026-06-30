class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        visited = [[False] * c for _ in range(r)]
        res = False

        def dfs(i, j, curr):
            if curr == len(word):
                return True
            
            if i < 0 or i >= r or j < 0 or j >= c or visited[i][j] or board[i][j] != word[curr]:
                return False
            
            visited[i][j] = True
            res = False
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                res = res or dfs(i+d[0], j+d[1], curr+1)
            visited[i][j] = False
            
            return res
        
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True

        return False
