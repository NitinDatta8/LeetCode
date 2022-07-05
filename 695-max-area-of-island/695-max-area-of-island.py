def dfs(grid, r, c): 
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0: 
            return 0 
         
        grid[r][c] = 0 
        
        up = dfs(grid, r-1, c)
        do = dfs(grid, r+1, c)
        le = dfs(grid, r, c-1)
        ri = dfs(grid, r, c+1)
        
        return up + do + le + ri + 1
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: 
                    max_size = max(dfs(grid, r, c), max_size)
                    
        return max_size 
    
    