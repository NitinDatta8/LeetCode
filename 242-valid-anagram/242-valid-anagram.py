class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs, ft = {}, {}
        for i in s: 
            fs[i] = 1 + fs.get(i,0)
        
        for i in t: 
            ft[i] = 1 + ft.get(i,0)
        
        if fs == ft: 
            return True 
        else:
            return False