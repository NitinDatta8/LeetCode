'''
enumerate over the list 
find element in current index and go to that index-1 and set it as negative
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i,v in enumerate(nums):
            nums[abs(v)-1] = abs(nums[abs(v)- 1]) *(-1)
        
        for i in range(len(nums)): 
            if nums[i] > 0: 
                res.append(i+1)
        
        return res