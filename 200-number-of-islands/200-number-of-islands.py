'''
maintain a count variable 
iterate over each cell using 2 for loops
if cell value is 1 do dfs
increment count by 1 
return count


DFS()
check boundary conditions and check if cell value is 0 then return 
set current cell as visited (mark it to 0)
do dfs() in all 4 directions
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1': 
                    dfs(r,c)
                    count += 1
        return count 