class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        freq1 , freq2 = {}, {}
        for i in range(k):
            freq1[s1[i]] = 1 + freq1.get(s1[i],0)
        
        l = 0 
        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r],0)
            if freq1 == freq2: 
                return True
            
            if r - l + 1 >= k: 
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0: 
                    del freq2[s2[l]]
                l += 1 
        return False
        
        