class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts,ends = [],[]
        for i in intervals: 
            starts.append(i[0])
            ends.append(i[1])
        
        starts.sort()
        ends.sort()
        available,num_rooms = 0,0 
        s,e = 0,0
        while s<len(starts):
            if starts[s]<ends[e]:
                if available == 0: 
                    num_rooms += 1
                else: 
                    available -= 1
                s += 1
            else: 
                available += 1
                e += 1
        return num_rooms