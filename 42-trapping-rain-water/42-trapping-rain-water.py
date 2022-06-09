# 4 2 0 3 2 5 
# 0 4 4 4 4 4 max_left 
# 5 5 5 5 5 0 max_right
# 0 4 4 4 4 0 x = min(max_left, max_right)
# 0 2 4 1 2 0 x - height[i]
class Solution:
    def trap(self, nums: List[int]) -> int:
        # step 1 
        max_left = [0] * len(nums)
        maxl = 0 
        for i in range(1,len(nums)):
            maxl = max(maxl,nums[i-1])
            max_left[i] = maxl
        
        # step 2
        max_right = [0] * len(nums)
        maxr = 0 
        for i in range(len(nums)-2, -1, -1 ):
            maxr = max(maxr,nums[i+1] )
            max_right[i] = maxr
        
        # step 3
        min_both = []
        for i,j in zip(max_left, max_right):
            min_both.append(min(i,j))
        
        res = []
        for i,j in zip(min_both,nums):
            val = i - j 
            if val < 0: 
                res.append(0)
            else: 
                res.append(val)
        return sum(res)