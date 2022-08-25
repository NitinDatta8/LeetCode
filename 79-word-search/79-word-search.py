'''
iterate over every cell and do dfs
dfs(r, c):
    if i == len(word) return True 
    boundary conditions and if word[i] != board[r][c] and (r,c) not in board
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i): 
            if i == len(word): 
                return True 
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r,c) in visited: 
                return False 
            
            visited.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))
            visited.remove((r,c))
            return res
        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r, c, 0): 
                    return True 
        return False