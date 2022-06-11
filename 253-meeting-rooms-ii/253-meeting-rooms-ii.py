# put them seperate and sort them 
# s = e= 0 
# compare start and end 
# [0   5 15]
# [10 20 30]
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        for i in intervals: 
            starts.append(i[0])
            ends.append(i[1])
            
        starts.sort()
        ends.sort()
        
        s, e = 0, 0 
        req = 0 
        maxreq = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                req += 1 
                s += 1
            else: 
                req -= 1
                e += 1
            maxreq = max(req, maxreq)
        return maxreq
            