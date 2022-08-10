'''
use backtracking and 2 conditions 
base case is when open count and close count are equal to n: 
    append to result and return
    
1. keep a check for max possible open paranthesis 
2. always make sure that open_count >= close_count

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(openN, closedN): 
            if openN == closedN == n: 
                res.append(''.join(stack))
                return 
            
            if openN < n: 
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN: 
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
            