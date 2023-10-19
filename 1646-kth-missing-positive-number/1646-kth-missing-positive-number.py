'''
Brute Force: O(n) complexity
1. Create count which tracks count of integers not present in arr. 
2. Return the number if its k

Less than O(n)
1. Let us use current array and its indices to come up with a new array. 
This will give us number of missing elements upto that point. 

## arr[i] - i - 1
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 0
        e = len(arr)

        while s < e: 
            m = (s + e) // 2
            if arr[m] - 1 - m < k: 
                s = m + 1
            else: 
                e = m 
        return s + k