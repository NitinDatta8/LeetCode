
'''
use BFS
maintain time and fresh oranges
use 2 for loops to iterate over every cell of grid and keep count of fresh oranges at the same time add rotten oranges to queue
run over queue and popleft 
use for loop and check adjacent cells mark 1s to 2s and append to queue and reduce fresh 
increase time 
return time if fresh == 0 or -1
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0 
        fresh = 0 
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    fresh += 1
                elif grid[r][c] == 2: 
                    q.append([r,c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0: 
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions: 
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1