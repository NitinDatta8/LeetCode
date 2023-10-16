class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        s, e = 0, len(nums) - 1
        while s <= e: 
            mid = (s + e) // 2
            if nums[mid] >= target: 
                e = mid - 1
            elif nums[mid] < target: 
                s = mid + 1

        print(s, e)
        f = 0
        x = s
        while -1 < s < len(nums) and nums[s] == target: 
            f = 1
            s += 1
        if f == 1: 
            res[0] = x
            res[1] = s - 1
        else: 
            return res
        
        return res