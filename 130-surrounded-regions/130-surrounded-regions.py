'''
run 2 for loops and iterate over every cell 
if cell is 'O' and is on the border run a DFS
DFS is used to mark the cells connected to border 'O' cell 

in DFS()
    check for border conditions and check if cell is not marked 'X' and return for these cases 
    mark current cell as 'V' 
    run dfs on all 4 directions
    
run 2 for loops again and convert all 'O's to X and all 'V's to 'O'
'''
        
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c): 
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 'O':
                return 
            grid[r][c] = 'V'
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
            
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'O' and (r in [0, ROWS-1] or c in [0,COLS-1]): 
                    dfs(r,c)
                    
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                elif grid[r][c] == 'V':
                    grid[r][c] = 'O'
        