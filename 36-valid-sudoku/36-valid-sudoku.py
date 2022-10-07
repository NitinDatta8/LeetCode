class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        create 3 sets 
        iterate over every cell using 2 for loops 
        if . then continue 
        check if already in any one of the three set return False 
        add to all the sets 
        end return true
        '''
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if board[r][c] == '.':
                    continue 
                
                if (board[r][c] in rows[r]
                   or board[r][c] in cols[c] or 
                   board[r][c] in squares[r//3, c//3]): 
                    return False 
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True