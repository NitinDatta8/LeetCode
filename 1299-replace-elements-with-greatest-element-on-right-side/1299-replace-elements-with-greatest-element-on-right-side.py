'''
store last element in cur_max and replace with -1
iterate backwards from second last element 

'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = arr[-1]
        res = []
        for i in range(len(arr)-1, -1, -1): 
            if arr[i] > cur_max: 
                cur_max = arr[i]
            
            res.append(cur_max)
        
        res.pop()
        res = res[::-1]
        res.append(-1)
        return res
        