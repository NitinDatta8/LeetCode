'''
start from left and maintain max_left till that point 
start from right and maintain max_right till that point
take min of these 2 at certain index and remove the height from it 
'''
class Solution:
    def trap(self, nums: List[int]) -> int:
        max_left = [1] * len(nums)
        max_right = [1] * len(nums)
        max_l, max_r = 0, 0 
        for i in range(len(nums)): 
            max_l = max(max_l, nums[i])
            max_left[i] = max_l 
        
        for i in range(len(nums)-1, -1, -1): 
            max_r = max(max_r, nums[i])
            max_right[i] = max_r
        
        ans = 0
        for i in range(len(nums)): 
            min_val = min(max_left[i], max_right[i])
            ans += min_val - nums[i]
            
        return ans
            