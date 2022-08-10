'''
add numbers to stack 
if anything other than number comes pop top 2 elements of stack and perform the operation 
add the res back to stack and continue 
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens: 
            if t not in '+-*/': 
                stack.append(int(t))
            else: 
                e1 = int(stack.pop())
                e2 = int(stack.pop())
                if t == '+': 
                    stack.append(e1 + e2)
                elif t == '-': 
                    stack.append(e2 - e1)
                elif t == '*': 
                    stack.append(e1 * e2)
                elif t == '/':
                    stack.append(int(float(e2)/e1))
        return stack.pop()