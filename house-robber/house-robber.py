class Solution:
    def dp(self,nums,n):
        # Base condition
        if n==0:
            return nums[0]
        if n==1:
            return max(nums[0],nums[1])
        
        # Choice diagram or recurrence relation
        if n not in self.memo:
            self.memo[n] = max(self.dp(nums,n-1), nums[n]+ self.dp(nums,n-2))
        return self.memo[n]
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.dp(nums,len(nums)-1)
        
        