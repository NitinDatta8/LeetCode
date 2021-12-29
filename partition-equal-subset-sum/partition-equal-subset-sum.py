class Solution:
    def subset_sum(self,weights,W,n):
        t = [[None for i in range(W+1)] for j in range(n+1)]

        for i in range(n+1):
            for j in range(W+1):
                t[0][j] = False 
                t[i][0] = True

                if j < weights[i-1]:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = t[i-1][j] or t[i-1][j-weights[i-1]]

        return t[n][W]   
    
    def canPartition(self, nums: List[int]) -> bool:
        even_sum = 0 
        for i in nums:
            even_sum += i 
        
        if even_sum % 2 != 0: 
            return False 
        
        check_sum = even_sum//2
        if check_sum in nums: 
            return True 

        return self.subset_sum(nums,check_sum,len(nums))
    
    