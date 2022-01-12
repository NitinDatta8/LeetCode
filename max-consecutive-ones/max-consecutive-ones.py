class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,maxcount = 0,0
        for i in nums: 
            if i==1:
                count +=1
            else:
                maxcount = max(maxcount,count)
                count = 0
        return max(count,maxcount)