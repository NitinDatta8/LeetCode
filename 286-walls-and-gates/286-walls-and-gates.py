
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        visited = set()
        ROWS, COLS = len(rooms), len(rooms[0])
        
        def addrooms(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or rooms[r][c] == -1 or (r,c) in visited: 
                return 
            visited.add((r,c))
            q.append([r,c])
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        
        dist = 0
        while q: 
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist 
                addrooms(r+1, c)
                addrooms(r-1, c)
                addrooms(r, c+1)
                addrooms(r, c-1)
            dist += 1