# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        s = 0
        e = abs(reader.get(0))+abs(target)+1
        while s<=e:
            m = (s+e)//2
            val = reader.get(m)
            print(s,m,e,val)
            if val == target:
                return m
            elif val > target:
                e = m - 1
            else:
                s = m + 1
        return -1
        