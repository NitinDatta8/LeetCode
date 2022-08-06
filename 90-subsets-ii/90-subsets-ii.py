'''
Time: O(n 2^n) - to create power set we meed 2^n lists and each list can be max length of n
Space: O(n 2^n) - same as time 
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(i, subset): 
            if i == len(nums): 
                res.append(subset[:])
                return 
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return res