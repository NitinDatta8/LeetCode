'''
time O(nm 4^len(word))
iterate over every cell of board and do dfs
if dfs(): return True 
dfs(r, c, i): 
    check base case - if i == len(word): return True
    check boundary conditions and word[i]!= board[r][c] and (r,c) should not be visited (to avoid infinite loops) - return False 
    add current coordinates to visited set
    do dfs in all 4 directions 
    return res
return False 
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, i): 
            if i == len(word): 
                return True 
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c]!= word[i] or (r,c) in visited: 
                return False 
            
            visited.add((r,c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visited.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS): 
                if dfs(r, c, 0):
                    return True 
        return False
                    