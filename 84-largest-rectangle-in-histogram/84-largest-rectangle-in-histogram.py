'''
main idea - if we see a smaller height coming next to a larger height it means we cannot extend the previous height 
maintain a stack with index and height 
if current height less than previous height pop the previous height and update the max_area 
at the same time move current_heights start index back to prev_heights index

at end stack is still not empty it means that the current elements in the stack have been  extended 
we need to check if they can form the max_area 
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # store index and height
        max_area = 0
        for i, h in enumerate(heights): 
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack: 
            max_area = max(max_area, h * (len(heights) - i))
        return max_area