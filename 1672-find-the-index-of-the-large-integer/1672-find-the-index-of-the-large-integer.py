# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        s = 0 
        e = reader.length() - 1
        while s <= e: 
            m = (s + e) // 2
            length = e - s 
            print(s, e, m, length)
            if length == 0: 
                return s
            if length % 2 == 0: 
                val = reader.compareSub(s, m - 1, m + 1, e)
                if val == 0: 
                    return m 
                elif val == -1: 
                    s = m + 1
                elif val == 1: 
                    e = m - 1
            else: 
                val = reader.compareSub(s, m, m + 1, e)
                if val == 0:
                    return m
                elif val == -1: 
                    s = m + 1
                elif val == 1: 
                    e = m
        # n = reader.length()
        # s = 0
        # e = n-1
        # while s<=e:
        #     m=(s+e)//2
        #     length = e - s + 1
        #     if length % 2 == 0:
        #         x = m+1 if m+1 <= e else e
        #         print("e",s,m,x,e)
        #         res = reader.compareSub(s,m,x,e)
        #         if res == 0:
        #             return m
        #         elif res == 1:
        #             e = m
        #         else:
        #             s = m + 1
        #     else:
        #         r = m-1 if m-1 >= s else s
        #         x = m+1 if m+1 <= e else e
        #         print("o", s,r,x,e)
        #         res = reader.compareSub(s,r,x,e)
        #         if res == 0:
        #             return m
        #         elif res == 1:
        #             e = m - 1
        #         else:
        #             s = m + 1