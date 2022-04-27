class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        l = r = 0 
        res = []
        while r < len(nums):
            # pop smaller values from deque
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            
            # remove the left value out of window
            if l > d[0]:
                d.popleft()
                 
            if r+1 >=k:
                res.append(nums[d[0]])
                l += 1
            r += 1
            
        return res
            