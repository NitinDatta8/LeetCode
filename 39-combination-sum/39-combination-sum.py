'''
Time: O(2^target) - the reason is because when we create the tree we can go maximum till the target value where our base case stops if it goes more
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total): 
            if total == target: 
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            # Case 1 where we add the element
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            # Case 2 go down without adding the current element 
            cur.pop()
            dfs(i + 1, cur, total)
        
        
        dfs(0, [], 0)
        return res