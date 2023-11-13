'''
[1]
1
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        max_profit = 0 
        s = prices[0]

        for i in range(1, len(prices)): 
            if prices[i] < s: 
                s = prices[i]
        
            profit = prices[i] - s
            max_profit = max(max_profit, profit)
        return max_profit

