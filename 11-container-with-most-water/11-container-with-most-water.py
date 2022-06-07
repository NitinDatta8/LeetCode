# use 2 pointers l and r 
# find min of the 2 heights -> multiply with distance on x axis (r - l + 1)
# if l < r: l ++ elif l > r: r-- 
# maintain maxwater
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxwater = -1 * math.inf
        while l < r: 
            water = min(height[l], height[r]) * (r - l)
            maxwater = max(maxwater, water)
            
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return maxwater