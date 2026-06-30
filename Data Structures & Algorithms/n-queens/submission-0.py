class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        grid = [['.'] * n for _ in range(n)]
        colSet = set()
        posDiag = set()
        negDiag = set()

        def dfs(r):
            if r == n:
                queens = []
                for row in grid:
                    queens.append("".join(row))
                
                res.append(queens)
                return 
            
            # going through every column
            for c in range(n):
                if ((c not in colSet) 
                and ((r + c) not in posDiag) 
                and ((r - c) not in negDiag)):
                   grid[r][c] = 'Q'
                   colSet.add(c)
                   posDiag.add(r+c)
                   negDiag.add(r-c)

                   dfs(r+1)

                   grid[r][c] = '.'
                   colSet.remove(c)
                   posDiag.remove(r+c)
                   negDiag.remove(r-c)

        dfs(0)
        return res

