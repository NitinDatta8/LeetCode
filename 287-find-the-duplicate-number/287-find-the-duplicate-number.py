class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                return nums[i]
            else: 
                freq[nums[i]] =1 
