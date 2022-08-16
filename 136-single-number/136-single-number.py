class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # do XOR on each number 
        res = 0 
        for n in nums: 
            res = n ^ res 
        return res