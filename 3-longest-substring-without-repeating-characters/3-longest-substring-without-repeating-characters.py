class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0 
        l = 0 
        maxlen = -1
        freq = {}
        for r in range(len(s)):
            if s[r] not in freq: 
                freq[s[r]] = 1
            else: 
                maxlen = max(maxlen,r-l)
                while s[r] in freq: 
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0: 
                        del freq[s[l]]
                    l += 1
                freq[s[r]] = 1
        return max(maxlen, r-l+1)