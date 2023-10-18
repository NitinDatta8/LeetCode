class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1
        e = x 
        while s <= e: 
            m = (s + e) // 2
            if x // m == m: 
                return m 
            elif x // m < m: 
                e = m - 1
            else: 
                s = m + 1
        return e