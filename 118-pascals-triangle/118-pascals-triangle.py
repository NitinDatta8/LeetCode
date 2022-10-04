class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1,1]]
        if numRows == 1: 
            return [[1]]
        elif numRows == 2: 
            return triangle 
        
        for i in range(numRows-2): 
            cur = triangle[-1]
            new_cur = [1]
            for i in range(len(cur)-1):
                new_cur.append(cur[i] + cur[i + 1])
            
            new_cur.append(1)
            triangle.append(new_cur)
        
        return triangle
                