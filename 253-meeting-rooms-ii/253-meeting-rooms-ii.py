'''
0  5  15
10 20 30
res = 2 

'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        for s, e in intervals: 
            starts.append(s)
            ends.append(e)
        
        starts.sort()
        ends.sort()
        occupied = 0 
        max_occupied = 0 
        s, e = 0, 0
        while s < len(starts): 
            if starts[s] < ends[e]:
                occupied += 1
                max_occupied = max(occupied, max_occupied)
                s += 1
            else: 
                occupied -= 1
                e += 1
        return max_occupied