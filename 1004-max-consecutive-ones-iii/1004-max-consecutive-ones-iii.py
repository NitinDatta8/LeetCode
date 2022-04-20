class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,res, maxc = 0,0,0
        for r in range(len(nums)):
            if nums[r] == 1: 
                maxc += 1
            
            if r - l + 1 - maxc > k: 
                if nums[l] == 1: 
                    maxc -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res
                    