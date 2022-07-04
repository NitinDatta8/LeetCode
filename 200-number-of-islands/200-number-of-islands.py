'''
loop through every element of the grid
call explore function if grid[r][c] is not equal to "0"
check if the grid[r][c] is not visited: 
and set count to 1

return the count

EXPLORE function
check for edge cases like right left top down  boundaries
call BFS on the current cell 
mark it as visited and explore the whole island and mark them as visited


'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0 
        for r in range(len(grid)): 
            for c in range(len(grid[0])):
                cur = grid[r][c]
                # cur_name = str(r) + ',' + str(c)
                if self.explore(grid,r,c,visited) == True:
                    count += 1
        
        return count 
    
    def explore(self, grid, r, c, visited):
        cur_name = str(r) + ',' + str(c)
        rowinbounds = 0 <= r and r < len(grid)
        colinbounds = 0 <= c and c < len(grid[0])
        
        if not rowinbounds or not colinbounds: 
            return False 
        
        if grid[r][c] == "0": return False 
        
        if cur_name in visited: return False 
        visited.add(cur_name)
        
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)
        return True