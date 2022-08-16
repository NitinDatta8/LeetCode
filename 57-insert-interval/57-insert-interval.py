'''
need to check 3 main condition 
no overlap and smaller than current interval 
    put newinterval into result and put rest all intervals after it 
no overlap and bigger than current interval 
    put current interval into result
overlap condition
    modify newinterval = min(newinterval[0], interval[0]), max(newinterval[1], interval[1])

at end add newinterval and return
we do not add newinterval as soon as its modified because it is possible that they might be merged again incase of overlap
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)): 
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])
            else: 
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
        return res
