class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: 
            return True
        s = 1 
        e = num // 2
        while s <= e: 
            m = (s + e) // 2
            if m *m == num: 
                return True 
            elif m*m < num:
                s = m + 1
            else: 
                e = m - 1
        return False