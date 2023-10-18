class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        while s <= e: 
            m = (s + e) // 2
            if nums[s] <= nums[m]: 
                if nums[s] > nums[e]: 
                    s = m + 1    
                else: 
                    return nums[s]                                               
            elif nums[s] > nums[m]: 
                e = m
            print(s, e, m)
