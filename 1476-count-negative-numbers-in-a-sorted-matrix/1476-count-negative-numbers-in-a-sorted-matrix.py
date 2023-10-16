class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)): 
            s, e = 0, len(grid[0]) - 1
            while s <= e: 
                mid = (s + e) // 2
                if grid[i][mid] >= 0: 
                    s = mid + 1 
                elif grid[i][mid] < 0:  
                    e = mid - 1
            print(s, e, mid)     
            count += len(grid[i]) - s
        
        return count