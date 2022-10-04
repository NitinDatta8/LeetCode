class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = []
        i, j = 0, 0 
        while i < len(s) and j < len(t): 
            if s[i] == t[j]:
                res.append(t[j])
                i += 1
                j += 1
            else: 
                j += 1 
        print(res)
        if res == list(s): 
            return True 
        else: 
            return False