'''
maintain result that is a list 
do backtracking
backtrack(i): 
    base condition - if i >= len(s): append(copy) to res and return 
    
    iterate from i to len(s) with j
    if ispali(s, l, r): 
        copy.append(s[i:j + 1])
        backtrack(j + 1)
        copy.pop()

backtrack(0)
return res
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        copy = []
        
        def backtrack(i): 
            if i >= len(s): 
                res.append(copy[:])
                return res
            
            for j in range(i, len(s)): 
                if self.ispali(s, i, j):
                    copy.append(s[i:j + 1])
                    backtrack(j + 1)
                    copy.pop()
        
        backtrack(0)
        return res
    
    def ispali(self, s, l, r): 
        while l < r: 
            if s[l] != s[r]: 
                return False 
            l += 1
            r -= 1
        return True
        