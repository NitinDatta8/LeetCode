
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        left = []
        right = []
        for i in intervals:
            left.append(i[0])
            right.append(i[1])
        left.sort()
        right.sort()

        l = 0
        r = 0
        roomsMax = 0 
        rooms = 0
        while l < len(left):
            if left[l] < right[r]:
                rooms += 1
                l += 1
            else:
                rooms -= 1
                r += 1
            roomsMax = max(roomsMax, rooms)
        
        return roomsMax

            