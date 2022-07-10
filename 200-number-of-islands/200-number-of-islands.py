'''
count = 0 
2 for loops to check the grid
if grid[r][c] == '1':
    dfs(r,c)
    count += 1

return count

dfs(r,c):
check for boundary conditions and grid[r][c] !='0' return 
grid[r][c] = '0'

dfs(r+1, c)
dfs(r-1, c)
dfs(r, c+1)
dfs(r, c-1)
return

Time - O(m*n)
Space - O(1)
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return 
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
        return count