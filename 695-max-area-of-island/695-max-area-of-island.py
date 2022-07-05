class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c): 
            if r < 0 or c < 0 or r >=len(grid) or c >= len(grid[0]) or grid[r][c]==0:
                return 0 
            
            grid[r][c] =0
            
            size = 1 
            size += dfs(r-1, c)
            size += dfs(r+1, c)
            size += dfs(r, c-1)
            size += dfs(r, c+1)
            
            return size
            
        max_size = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: 
                    size = dfs(r,c)
                    max_size = max(max_size, size)
        
        return max_size