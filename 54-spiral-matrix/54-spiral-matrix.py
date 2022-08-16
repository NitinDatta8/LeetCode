'''
maintain top, bottom, left and right 
maintain output and keep appending to it 
check if l<r and t<b: 
    iterate over top row and add 
    increment top
    
    iterate over right column and add 
    decrement right
    
    check boundary conditions 
    iterate over bottom row in reverse and add 
    decrement bottom 
    
    iterate over left row in reverse and add 
    increment left
    
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom: 
            # add top row
            for i in range(left, right): 
                res.append(matrix[top][i])
            top += 1
            
            # add right column 
            for i in range(top, bottom): 
                res.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and top < bottom): 
                break 
            
            # add bottom row in reverse
            for i in range(right-1, left -1, -1):
                res.append(matrix[bottom -1][i])
            bottom -= 1
            
            # add left column in reverse
            for i in range(bottom -1, top-1, -1): 
                res.append(matrix[i][left])
            left += 1
        return res
            
                