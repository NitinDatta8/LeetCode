'''
iterate over every cell in the grid 
if cell is 1 then we do a DFS
DFS - traverse all 4 directions and find area recursively 
max_area = max(max_area, area)

return max_area
visited = set()
DFS(): 
    boundary condtions + if cell is not water + cell should not be visited 
    mark cell as visited 

    area is incremented and do dfs in all 4 directions
TIME - O(nm)
SPACE - O(1)
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0 
        
        def dfs(r, c):
            # boundary and other edge conditions
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0: 
                return 0 
            
            grid[r][c] = 0 
            
            area = 1 
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    area = dfs(r, c)
                    max_area = max(max_area, area) 
                    
        return max_area