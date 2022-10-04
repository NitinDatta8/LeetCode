'''
store last element in cur_max and replace with -1
iterate backwards from second last element 

'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1 
        
        for i in range(len(arr)-1, -1, -1): 
            new_max = max(right_max, arr[i])
            arr[i] = right_max 
            right_max = new_max 
        return arr
        