class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        visited = set()

        def dfs(i, j, k):
            nonlocal r, c
            if k == len(word): return True 
            if min(i, j) < 0 or i >= r or j >= c or (i, j) in visited or board[i][j] != word[k]:
                return False 

            visited.add((i, j))
            res = (dfs(i+1, j, k+1) or 
                   dfs(i-1, j, k+1) or 
                   dfs(i, j+1, k+1) or 
                   dfs(i, j-1, k+1))
            visited.remove((i, j))
            return res 
            
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0): return True

        return False
