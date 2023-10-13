class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        nums = [[0] * n for i in range(m)]
        for r, c in indices: 
            for i in range(n): 
                nums[r][i] += 1
            for j in range(m): 
                nums[j][c] += 1
        
        count = 0
        for r in range(m): 
            for c in range(n): 
                if nums[r][c] % 2 != 0: 
                    count += 1
        return count