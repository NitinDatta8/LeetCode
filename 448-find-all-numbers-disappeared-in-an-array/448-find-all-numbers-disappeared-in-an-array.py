class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in n: 
                res.append(i)
        return res