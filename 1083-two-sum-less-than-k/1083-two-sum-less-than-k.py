class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # if len(nums) == 1:
        #     return -1
        # nums.sort()
        nums.sort()
        res = 0
        for i in range(len(nums)-1):

            s = i+1
            e = len(nums)-1
            while s <= e:
                m = (s+e)//2
                add = nums[i] + nums[m]
                if add < k:
                    res = max(res,add)
                    s = m + 1
                else:
                    e = m - 1

        return res if res != 0 else -1
        
