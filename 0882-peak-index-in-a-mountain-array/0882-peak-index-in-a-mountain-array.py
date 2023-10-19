'''
0 1 2 3 1 0 
s   m     e  



[3,4,5,1]
s  m    e
'''


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s, e = 1, len(arr) -1
        while s<=e:
            m = (s + e) // 2
            if arr[m-1] < arr[m] and arr[m] > arr[m+1]: 
                return m 
            elif arr[m-1] < arr[m] < arr[m+1]: 
                s = m + 1
            elif arr[m-1] > arr[m] > arr[m+1]: 
                e = m - 1
            print(s, e, m)