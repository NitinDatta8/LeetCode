'''
Time - O(n 2^n)
recursively add the current element to the subset or do not add it 
do it in the form of a decision tree
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            if i >= len(nums): 
                res.append(subset[:])
                return 
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res