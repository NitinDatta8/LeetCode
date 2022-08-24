'''
1. iterate over every cell and store where are the gates  and store them in a queue - (r,c)
2. BFS(): 
    check for boundary conditions and check for walls and check for visited condition
    pop left element from queue and traverse in 4 directions and maintain distance and replace inf with the dist

q = [(0,2) (3,0)]
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        ROWS, COLS = len(rooms), len(rooms[0])
        for r in range(ROWS): 
            for c in range(COLS): 
                if rooms[r][c] == 0: 
                    q.append([r,c])
        
        dist = 1
        while len(q) > 0: 
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions: 
                    row, col = r + dr, c + dc
        
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or rooms[row][col] == -1 or rooms[row][col]!= 2147483647: 
                        continue
                    
                    rooms[row][col] = dist 
                    q.append([row, col])
            dist += 1

                