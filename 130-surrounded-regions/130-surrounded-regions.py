'''
check boundaries and run dfs if value is O 
to mark them set them as V 

at end go through every cell and check if its V mark them as O other all mark as X
'''
        
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c): 
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 'O': 
                return 
            grid[r][c] = 'V' 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if r in [0, ROWS-1] or c in [0, COLS-1]: 
                    if grid[r][c] == 'O': 
                        dfs(r,c)
                    
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 'V':
                    grid[r][c] = 'O'
                else: 
                    grid[r][c] = 'X'