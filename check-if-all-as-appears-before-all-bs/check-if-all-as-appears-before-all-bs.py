class Solution:
    def checkString(self, s: str) -> bool:
        if len(set(s)) == 1:
            return True
        val_a, val_b = 0,0
        for i,x in enumerate(s):
            if x == 'a':
                val_a = i 
        for i,x in enumerate(s):
            if x == 'b':
                val_b = i
                break
        
        if val_a<val_b:
            return True
        else:
            return False