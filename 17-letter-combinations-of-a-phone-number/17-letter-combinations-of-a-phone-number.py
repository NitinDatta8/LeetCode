'''
make hashmap to map corresponding chars
backtrack(i, curstr):
    # base case 
    if len(curstr) == len(digits):
        res.append(curstr)
        return
    
    for c in digit_to_char[digits[i]]:
        backtrack(i + 1, curstr + c)
    
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
        
        def backtrack(i, curstr): 
            # base case 
            if len(curstr) == len(digits):
                res.append(curstr)
                return

            for c in digit_to_char[digits[i]]:
                backtrack(i + 1, curstr + c)
        if digits: 
            backtrack(0, '')
        return res