# 1 3 5 4 3 2 1
# 1 4 5 3 3 2 1
# iterate backwards and check where the number is lesser 
# that is pivot if pivot is 0 nums.sort() and return 
# then again start from end and check where value > pivot 
# swap pivot with that value
# sort the numbers after pivot
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0 
        for i in range(len(nums)-1, 0, -1): 
            if nums[i-1] < nums[i]: 
                pivot = i
                break 
                
        if pivot == 0: 
            nums.sort()
            return 
        
        r = len(nums)-1
        while nums[pivot-1] >= nums[r]:
            r -= 1
        
        nums[pivot-1], nums[r] = nums[r], nums[pivot-1]
        nums[pivot:] = sorted(nums[pivot:])
                