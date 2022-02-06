class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0: 
            return nums 
        def reverse(start,end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        k %= len(nums)
        end = len(nums)-1
        reverse(0,end-k)
        reverse(end-k+1, end)
        reverse(0,end)
        return nums