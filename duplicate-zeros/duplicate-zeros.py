class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i<=len(arr)-1:
            if arr[i] == 0:
                arr[i+1:] = arr[i:-1]
                i += 2
            else: 
                i += 1
        
        