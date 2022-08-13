'''
sort based on start value
iterate over each interval 
check if end of current >= start of next: 
    return False 
return true at end
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1): 
            if intervals[i][1] > intervals[i + 1][0]: 
                return False
        return True
        
        