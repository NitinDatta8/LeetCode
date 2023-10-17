# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        s= 0 
        e = 2**31 - 1
        ans = -1
        while s <= e: 
            m = (s + e) // 2  
            # print(s, e, m, reader.get(m))
            if reader.get(m) == target: 
                return m 
            elif reader.get(m) > target: 
                e = m - 1
            else: 
                s = m + 1
    
        return -1