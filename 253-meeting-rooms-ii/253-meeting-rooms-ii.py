# 0  5  15 
# 10 20 30
# 1  2  1  

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts,ends = [],[]
        for inter in intervals: 
            starts.append(inter[0])
            ends.append(inter[1])
        
        starts.sort()
        ends.sort()
        required = 0 
        s, e = 0, 0 
        max_required = 0 
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                required += 1
            else: 
                e += 1
                required -= 1
            max_required = max(max_required, required)
        return max_required
                
            
            