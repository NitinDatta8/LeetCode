'''
use BFS 
maintain time and fresh oranges
in first 2 loops count fresh oranges and add rotten oranges to a queue
run the queue and popleft and use for loop to check adjacent cells 
change adjacent 1s to 2s and append to queue 
reduce fresh 
increase time 
return time if fresh == 0 else -1
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()
        
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1: 
                    fresh += 1
                
                if grid[r][c] == 2: 
                    q.append([r,c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c]==0 or grid[r][c]==2: 
                        continue

                    grid[r][c] = 2
                    q.append([r,c])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
        
 