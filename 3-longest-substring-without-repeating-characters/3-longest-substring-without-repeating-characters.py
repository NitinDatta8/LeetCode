class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ": return 1
        freq = {}
        left, maxlen = 0,0
        for i in range(len(s)):
            if s[i] not in freq: 
                freq[s[i]] = 1
            else: 
                while s[i] in freq: 
                    maxlen = max(maxlen, i-left)
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0: 
                        del freq[s[left]]
                    left += 1
                freq[s[i]] = 1
        return max(maxlen,len(s)-left)