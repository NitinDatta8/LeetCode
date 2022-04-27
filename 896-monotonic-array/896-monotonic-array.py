class Solution:
    def check_des(self, nums):
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
        return True
    
    def check_asc(self, nums):
        for i in range(len(nums)-1):
            if nums[i]> nums[i+1]:
                return False
        return True
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] > nums[-1]:
            return self.check_des(nums)
        else: 
            return self.check_asc(nums)
        