
        
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c): 
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] != 'O': 
                return 

            grid[r][c] = 'T' 

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='O' and (r in [0, len(grid)-1] or c in [0, len(grid[0])-1]): 
                    dfs(r, c)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                if grid[r][c] == 'T':
                    grid[r][c] = 'O'
                else: 
                    grid[r][c] = 'X'