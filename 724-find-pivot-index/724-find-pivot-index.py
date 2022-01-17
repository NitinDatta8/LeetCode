class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0 
        sums = sum(nums)
        for i in range(len(nums)):
            sums -= nums[i]
            if sums == leftsum: 
                return i 
            leftsum += nums[i]
            # print(sums,leftsum)
        return -1