# Better solution 
# Hashmap - store index as value and element as the key 
# check if target - element is present already as a key : YES then return current index+1 and value(index) of target-element  


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(numbers)): 
            if target - numbers[i] in freq: 
                return [freq[target-numbers[i]]+1,i+1] 
            else: 
                freq[numbers[i]] = i