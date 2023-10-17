class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        pairs = []
        for i, x in enumerate(intervals): 
            pairs.append([x, i])
        
        pairs.sort()
        res = [-1] * len(intervals)
        for i, p in enumerate(pairs): 
            end = p[0][1]
            s = i 
            e = len(pairs) - 1
            while s <= e: 
                mid = (s + e) // 2
                if pairs[mid][0][0] >= end: 
                    e = mid - 1
                else: 
                    s = mid + 1
            if -1 < s < len(pairs):
                res[pairs[i][1]] = pairs[s][1]
        return res
