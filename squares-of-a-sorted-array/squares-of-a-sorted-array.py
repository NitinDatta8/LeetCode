class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0,len(nums)-1
        squared = []
        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                squared.append(nums[i]**2)
                i += 1
            else: 
                squared.append(nums[j]**2)
                j -= 1
        return squared [::-1]