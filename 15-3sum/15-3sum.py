# sort the nums 
# iterate over nums and inside use while loop with l and r pointers to get the rest 2 numbers that add to 0 
# check for duplicates and remove them 
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