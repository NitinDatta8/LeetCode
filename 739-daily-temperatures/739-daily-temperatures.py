class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                x = stack.pop()
                res[x] = i - x
            stack.append(i)
        return res
        