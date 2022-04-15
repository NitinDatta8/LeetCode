class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0 
        run_sum = 0
        min_len = math.inf
        for i in range(len(nums)):
            run_sum += nums[i]
            while run_sum >= target: 
                min_len = min(min_len,i-start+1)
                run_sum -= nums[start]
                start +=1 
            
        if min_len == math.inf: 
            return 0 
        else: 
            return min_len