'''
Time - O(n 2^n)
recursively add the current element to the subset or do not add it 
do it in the form of a decision tree
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i): 
            # base case
            if i >= len(nums): 
                res.append(subset.copy())
                return 
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        
    