'''
  
1-------3
1---2 
    2---3
        3---4
        
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 
        prev_end = intervals[0][1]
        
        for start, end in intervals[1:]: 
            if start >= prev_end: 
                prev_end = end 
            else: 
                res += 1
                prev_end = min(end, prev_end)
        return res