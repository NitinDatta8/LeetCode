# 2,1,4,7,3,2,1,8,6
# 1. iterate i-1 < i > i + 1 
# 2. 2,1,4 
# left = i - 1
# while arr[left] < arr[left-1]: left -= 1
# min_left = left
# 3. 3,2,5 
# right = i + 1
# while arr[right] > arr[right+1]:right += 1
# min_right = right
# maxlen = max(maxlen, min_right - min_left + 1)

# find all peaks 
# find min_left, min_right of it 

# 1 2 3 4 5 
# [0,1,2,3,4,5,4,3,2,1,0] 

# [48,62,39]
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left, right = 0, 0 
        peak = 0
        maxlen = 0
        min_right = 0 
        min_left = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]: 
                peak = i
                
                left = i - 1
                while left > 0 and arr[left] > arr[left-1]: 
                    left -= 1 
                
                min_left = left
                
                right = i + 1
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right += 1
                
                min_right = right
                # print(min_left, min_right)
            maxlen = max(maxlen, min_right - min_left + 1)
            
        if min_right == 0 and min_left == 0: 
            return 0 
        else: 
            return maxlen