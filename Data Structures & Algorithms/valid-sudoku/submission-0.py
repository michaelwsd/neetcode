class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        diagSet = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue

                if board[i][j] in rowSet[i]: return False
                if board[i][j] in colSet[j]: return False
                if board[i][j] in diagSet[(i//3, j//3)]: return False

                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                diagSet[(i//3, j//3)].add(board[i][j])
        
        return True

