'''
sort my intervals based on first value 
iterate over each interval with a while loop 
if current interval ending >= next interval starting: 
    new_interval = [min(starts), max(ends)]
    intervals[i][0] = new_interval[0]
    intervals[i][1] = new_interval[1]
    del intervals[i+1]
else: 
    i += 1
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0 
        while i < len(intervals) -1: 
            if intervals[i][1] >= intervals[i + 1][0]: 
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                del intervals[i + 1]
            else: 
                i += 1
        return intervals