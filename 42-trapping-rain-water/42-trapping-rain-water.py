
#  [4, 2, 0, 3, 2, 5]
#1 [0, 4, 4, 4, 4, 4]
#2 [5, 5, 5, 5, 5, 0]
#3 [0, 4, 4, 4, 4, 0]
#4 [0, 2, 4, 1, 2, 0]
# sum of list of step 4 = 9 
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        min_lr = []
        res = []
        
        max_l = -1 
        max_r = -1 
        # Step 1
        for i in range(1,len(height)):
            max_l = max(max_l, height[i-1])
            max_left[i] = max_l 
        # Step 2
        for i in range(len(height)-2, -1, -1):
            max_r = max(max_r, height[i+1])
            max_right[i] = max_r
        
        # Step 3
        for i,j in zip(max_left, max_right):
            min_lr.append(min(i,j))
        
        # Step 4
        for i,j in zip(min_lr,height):
            val = i - j 
            if val < 0: 
                val = 0 
            res.append(val)
        return sum(res)
        
            