class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket,maxcount= 3,float('-inf')
        i,j=0,0
        freq = {}
        while i<len(fruits):
            if fruits[i]  not in freq: 
                basket -= 1
                if basket == 0: 
                    maxcount = max(maxcount,sum(freq.values()))
                    freq = {}
                    basket = 2
                    j += 1
                    i = j
                freq[fruits[i]] = 1
            else: 
                freq[fruits[i]] += 1
            i += 1
        return max(maxcount,sum(freq.values()))