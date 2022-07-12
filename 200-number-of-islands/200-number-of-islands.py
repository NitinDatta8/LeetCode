'''
maintain a count 
Use DFS if current cell has 1 
    in DFS mark all the connected 1s to 0 (visited) so that they arent counted again
    move all 4 directions recursively 
increment count once a full island is visited 
return the count 

Questions to ask: 
1. Will my input cells contain only 0/1? 
2. grid constraints whats the min/max size of rows or columns? 
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
        
        return count