'''
s = 0 
e = len(matrix)
-- binary search to find row to search 

-- run binary search on the row again to find if target is there
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix)-1
        while s <= e: 
            m = (s + e) // 2
            if matrix[m][0] == target: 
                return True
            elif matrix[m][0] >target: 
                e = m - 1
            else: 
                s = m + 1
        print(s, e, m)
        row = matrix[e]
        s, e = 0, len(row) - 1
        while s <= e: 
            m = (s+e) // 2
            if row[m] == target: 
                return True
            elif row[m] > target: 
                e = m - 1
            else: 
                s = m + 1
        return False

