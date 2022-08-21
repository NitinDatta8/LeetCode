'''
[0,0,1,1,1,0]
iterate over nums and store count for 0/1/2 in hashmap
res = {0:0, 1:, 2:2}

iterate over nums: 
check if res[0] > 0: 
    nums[i] = 0
    res[0] -= 1
elif res[1] > 0: 
    nums[i] = 1
    res[1] -= 1
else: 
    nums[i] = 2
    res[2] -= 1


O(n) - time
O(1) - space
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {}
        for i in range(len(nums)): 
            freq[nums[i]] = 1 +freq.get(nums[i], 0)
        
        for i in range(len(nums)): 
            if 0 in freq.keys() and freq[0] > 0:
                nums[i] = 0 
                freq[0] -= 1
            elif 1 in freq.keys() and freq[1] > 0: 
                nums[i] = 1
                freq[1] -= 1
            else: 
                nums[i] = 2
                freq[2] -= 1
                
            
            