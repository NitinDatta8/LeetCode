class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        freq_t, freq_s = {}, {}
        res = [-1,-1]
        l, minlen = 0,math.inf
        
        
        for i in range(len(t)): 
            freq_t[t[i]] = 1 + freq_t.get(t[i],0)
        have, need = 0, len(freq_t)
        for r in range(len(s)):
            freq_s[s[r]] = 1 + freq_s.get(s[r],0)
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                    have += 1
            
            while have == need: 
                if (r - l + 1) < minlen:
                    minlen = r - l + 1
                    res = [l,r]
                
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if minlen != math.inf else ""
                        
                        
                        