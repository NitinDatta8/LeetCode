class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        minimum_val = float('inf')
        for a,b in zip(nums[:4],nums[-4:]):
            minimum_val = min(minimum_val,b-a)
        return minimum_val
        # return min(b - a for a, b in zip(A[:4], A[-4:]))

        