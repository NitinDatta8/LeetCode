class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # hashmap of 2 elements only 
        # maintain left and right pointer 
        # remove elements from left when len(hashmap)>2
        # hasmap[1]: count
        # maxlen = max(r - l + 1, maxlen)
        
        freq = {}
        l = 0 
        maxlen = 0 
        for r in range(len(fruits)): 
            if fruits[r] not in freq: 
                freq[fruits[r]] = 1
            else: 
                freq[fruits[r]] += 1
                
            while len(freq) > 2: 
                maxlen = max(maxlen, r - l)
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
        return max(maxlen, r - l + 1)