class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq1,freq2 = {},{}
        for i in arr: 
            if i in freq1.values() or i in freq2.values():
                return True
            freq1[i] = i/2
            freq2[i] = i*2
            print(freq1,freq2)
        return False