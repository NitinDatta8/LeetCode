'''
Time : O(n n!)
Space: O(n!)
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1: 
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for p in perms: 
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        return res