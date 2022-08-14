'''
Time O(n m 4^len(word))
iterate over every cell and do dfs 
dfs()
    base case - if i == len(word): return True 
    check for boundary conditions and if (r,c) already in set and if word[i] is not the same char at board: continue 
    res = dfs in 4 directions 

return False
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i): 
            if i == len(word): 
                return True 
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r,c) in path: 
                return False
            
            path.add((r,c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r,c))            
            return res
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r, c, 0):
                    return True
        
        return False 
            