class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])

        def dfs(i, j):
            if min(i, j) < 0 or i >= r or j >= c or board[i][j] != 'O':
                return
            
            board[i][j] = 1
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(i+d[0], j+d[1])

        for i in range(c):
            if board[0][i] == 'O': dfs(0, i)
            if board[r-1][i] == 'O': dfs(r-1, i)
        
        for i in range(r):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][c-1] == 'O': dfs(i, c-1)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 1:
                    board[i][j] = 'O'
