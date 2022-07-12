'''
max_area to maintain maximum area 

iterate over grid using 2 for loops 
if a cell is found to be 1 perform dfs()

in dfs() 
    check boundary conditions and also check if current cell is not water and return 0
    set the  current cell as visited by changing its value to 0 
    size = 1
    call dfs recursively and add it to size
    return size

update max_area by checking max between max_area and size 
return max_area

Time: O(mn)
Space: O(1)
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0: 
                return 0 
            
            grid[r][c] = 0 
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
        
                    size = dfs(r,c)
                    max_area = max(max_area, size)
        
        return max_area