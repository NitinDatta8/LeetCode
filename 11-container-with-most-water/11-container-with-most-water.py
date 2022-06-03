# Brute force 
# Use 2 for loops to find all possible pairs 
# for every pair find the minimum and multiply with j - i (x axis length)
# Maintain a max_water variable that keeps updating if it finds a new maximum 

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_water = -1 
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 min_height = min(height[i], height[j])
#                 water = min_height * (j - i)
#                 max_water = max(max_water, water)
#         return max_water
    
# Optimal solution 
# use 2 pointers - 
# 1. go from left to right and find minimum(l,r) and reduce from right 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_water = -1 
        while l < r: 
            min_height = min(height[l], height[r])
            water = min_height * (r - l)
            max_water = max(max_water, water)
            if height[l] > height[r]:
                r -= 1
            else: 
                l += 1
        return max_water