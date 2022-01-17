
class Solution:
    from itertools import combinations
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        val = 0 
        nums.sort()
        for i in range(len(nums)-2):
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l<r: 
                check_zero = nums[i] + nums[l] + nums[r]
                if check_zero == 0: 
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif check_zero > 0: 
                    r -= 1
                else: 
                    l += 1
        return res
                    