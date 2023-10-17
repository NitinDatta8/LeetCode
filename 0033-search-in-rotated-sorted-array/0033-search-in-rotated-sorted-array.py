class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s <= e: 
            m = (s + e)// 2
            if nums[m] == target: 
                return m
            # left subarray 
            elif nums[s] <= nums[m]: 
                # 2 outer conditions
                if target < nums[s]  or  nums[m] < target:
                    s = m + 1
                else: 
                    e = m - 1
            elif nums[m] < nums[e]:
                if target < nums[m] or nums[e] < target:
                    e = m - 1
                else: 
                    s = m + 1
            
        return -1