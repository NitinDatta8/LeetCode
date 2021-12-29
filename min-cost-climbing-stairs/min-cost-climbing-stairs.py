class Solution:
    def minCost(self,cost,n):
        
        if n<0:
            return 0
        if n==0 or n==1:
            return cost[n]
        if n not in self.memo: 
            self.memo[n] = cost[n] + min(self.minCost(cost,n-1), self.minCost(cost,n-2))
        return self.memo[n]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.memo = {}
        return min(self.minCost(cost,n-1), self.minCost(cost,n-2))