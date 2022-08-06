'''
Time is O(2^n)
1. sort candidates to avoid duplicates later 
2. backtrack(pos, cur, target)
    3. if target becomes 0 then append to result list 
    4. if target  is less than or equal to 0 return 
    5. maintain previous = -1 and iterate from pos to last element in candidates 
    6. if curremt element equals to previous continue 
    7. append current elemnet to cur and call recursive backtrack(i +1, cur, target - candidates[i])
    8. pop the current element from cur and set prev to current element 
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