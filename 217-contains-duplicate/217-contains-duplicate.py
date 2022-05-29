class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq  = {}
        for i in nums: 
            if i not in freq: 
                freq[i] = 1
            else: 
                return True
        return False