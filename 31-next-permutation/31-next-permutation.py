# 1 3 5 4 3 2 1 
# we know index 1 needs to be swapped because right side of it everything is sorted in decreasing order 
# so index 1 or 3 is the pivot point 
# now start from right and find a point such that its greater than the pivot and swap with it 
# 1 4 5 3 3 2 1 
# now sort everything in ascending order after the pivot which should be next biggest number
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = 0
        # find the pivot 
        for i in range(n-1,0,-1):
            if nums[i-1] < nums[i]:
                pivot = i 
                break
        
        if pivot == 0: 
            nums.sort()
            return
        
        
        # find the swap which is first number greater than pivot 
        swap = n-1
        while nums[pivot-1] >= nums[swap]: 
            swap -= 1
        
        
        # swap 
        nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        # sort from pivot
        nums[pivot:] = sorted(nums[pivot:])