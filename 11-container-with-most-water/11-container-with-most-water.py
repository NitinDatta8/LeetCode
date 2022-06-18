# l r 
# 1,8,6,2,5,4,8,3,7 
# l               r
# min(l,r) * (r-l)
# if l < r: l ++ else r -- 
# max_area = max(max_area, area)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0 
        max_area = -1
        l, r = 0, len(height)-1
        while l < r: 
            min_height = min(height[l],height[r])
            area = min_height * (r - l) 
            max_area = max(max_area, area)
            if height[l] < height[r]: 
                l += 1
            else: 
                r -= 1
        return max_area