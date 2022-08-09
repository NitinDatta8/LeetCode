'''
Time is O(2^n)
1. sort candidates to avoid duplicates later 
ur and set prev to current element 
call backtrack and return result
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []
        def backtrack(pos, cur, target): 
            if target == 0: 
                res.append(cur[:])
            if target <= 0: 
                return 
            
            prev = -1
            for i in range(pos, len(candidates)): 
                if prev == candidates[i]: 
                    continue
                
                cur.append(candidates[i])
                backtrack(i + 1, cur, target - candidates[i])
                cur.pop()
                prev = candidates[i]
            
        backtrack(0, [], target)
        return res