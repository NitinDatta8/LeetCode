class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in points: 
            sq = sqrt(i[0]**2+i[1]**2)
            res.append((sq,i))
        res.sort()
        return [res[i][1] for i in range(k)]