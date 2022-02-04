# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        lo,hi = 1,n
        while lo<=hi:
            mid = lo +(hi-lo)//2
            if isBadVersion(mid) is False: 
                lo = mid+1
            elif isBadVersion(mid) is True:
                hi = mid-1
        return lo