class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i,val in enumerate(nums): 
            if target - val in freq: 
                return [freq[target-val], i]
            else:    
                freq[val] = i  
                
            