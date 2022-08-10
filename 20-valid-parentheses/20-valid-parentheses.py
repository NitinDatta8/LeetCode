class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['[', '{', '(']
        closed = [']', '}', ')']
        stack = []
        for c in s: 
            if c in opened: 
                stack.append(c)
            else: 
                if len(stack) != 0 and stack[-1] == opened[closed.index(c)]: 
                    stack.pop()
                else: 
                    return False 
        return len(stack) == 0