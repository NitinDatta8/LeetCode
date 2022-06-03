# Optimized solution
# 1. sort the list in ascending order 
# 2. use for loop to iterate over all elements - if ith and i-1th element is same then continue 
# 3. then use 2 pointer L and R to find triples that add to 0 --> add them to the result list 
# 4. Update the pointers carefully 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r: 
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0: 
                    r -= 1
                elif three_sum < 0: 
                    l += 1
                else: 
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res