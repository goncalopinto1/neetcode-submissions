from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for i in range(len(board)): # i represents the idx of each row

            for k in range(len(board[i])): # k represents the idx of each col

                if board[i][k] == ".": continue 

                if board[i][k] in rows[i] or board[i][k] in cols[k] or board[i][k] in grid[(i // 3, k // 3)]: return False
                
                rows[i].add(board[i][k])
                cols[k].add(board[i][k])
                grid[(i // 3, k // 3)].add(board[i][k])

        return True
