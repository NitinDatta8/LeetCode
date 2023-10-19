'''
Brute Force: O(n) complexity
1. Create count which tracks count of integers not present in arr. 
2. Return the number if its k
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur = 0 
        for i in range(1, arr[-1]+1+k):
            if cur < len(arr) and arr[cur] == i: 
                cur += 1
                
            else: 
                k -= 1
                if k == 0: 
                    return i