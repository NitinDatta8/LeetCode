class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minLeft = [float(inf)] * len(nums)
        minRight = [float(inf)] * len(nums)

        for i in range(len(nums)-1):
            cur = min(nums[i], minLeft[i])
            if cur < nums[i+1]: 
                minLeft[i + 1] = cur 
            else: 
                if cur == minLeft[i]: 
                    minLeft[i + 1] = float(inf)
                else: 
                    minLeft[i + 1] = minLeft[i]
        
        for i in range(len(nums)-1, 0, -1): 
            cur = min(nums[i], minRight[i])
            if cur < nums[i - 1]: 
                minRight[i - 1] = cur
            else: 
                if cur == minRight[i]: 
                    minRight[i - 1] = float(inf)
                else:
                    minRight[i - 1] = minRight[i]

        print(nums)
        print(minLeft)
        print(minRight)
        res = float(inf)
        for i in range(len(nums)): 
            res = min(res, nums[i] + minLeft[i] + minRight[i])
        
        return res if res != float(inf) else -1