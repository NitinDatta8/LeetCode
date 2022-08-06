'''
Time: O(2^target) - the reason is because when we create the tree we can go maximum till the target value where our base case stops if it goes more
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, cur, total):
            if total == target: 
                res.append(cur[:])
                return 
            
            if total > target or i >= len(candidates): 
                return 
            
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            
            cur.pop()
            backtrack(i + 1, cur, total)
            
        backtrack(0, [], 0)
        return res