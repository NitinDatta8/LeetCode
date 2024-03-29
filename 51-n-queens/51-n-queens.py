'''
queen moves in col, row, pos_diag and neg_diag
use backtracking - 
    iterate over row and check if (r,c) present in col, pos_diag or neg_diag
    if present continue
    add (r,c) to all 3 sets 
    set (r,c) to Q 
    backtrack()
    remove from sets 
    set (r,c) back to .
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag =set()
        res = []
        board = [['.'] * n for i in range(n)]
        def backtrack(r): 
            if r == n: 
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n): 
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag: 
                    continue
                
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = 'Q'
                
                backtrack(r + 1)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = '.'
        
        backtrack(0)
        return res