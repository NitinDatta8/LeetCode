class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)/2
        return int(total_sum - sum(nums))