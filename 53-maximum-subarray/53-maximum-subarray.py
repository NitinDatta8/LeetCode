class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        for n in nums[1:]:
            curSum = max(n, n+curSum)
            maxSum = max(maxSum, curSum)
        return maxSum