class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        i = 0 
        while i <len(nums)-1:
            if nums[i][1]>=nums[i+1][0] and nums[i][1]<nums[i+1][1]:
                nums[i][1] = nums[i+1][1]
                del nums[i+1]
            elif nums[i][1]>=nums[i+1][1]:
                del nums[i+1]
            else:
                i += 1
        return nums