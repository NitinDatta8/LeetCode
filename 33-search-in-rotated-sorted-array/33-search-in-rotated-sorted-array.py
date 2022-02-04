class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low<high:
            mid = (high+low)//2
            if target<nums[0]<nums[mid]:
                low = mid+1
            elif target>= nums[0]>nums[mid]:
                high = mid
            elif nums[mid]<target:
                low = mid +1
            elif nums[mid]>target:
                high = mid 
            else:
                return mid
        return -1