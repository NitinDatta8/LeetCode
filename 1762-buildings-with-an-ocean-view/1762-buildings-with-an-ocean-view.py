# Optimized
# Reverse iterate 
# store max till point and compare every element to that and add depending on it
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_t = -1 * math.inf
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_t:
                res.append(i)
                max_t = heights[i]
        return res[::-1]
        