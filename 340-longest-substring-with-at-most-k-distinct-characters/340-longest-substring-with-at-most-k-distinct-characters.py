class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, K: int) -> int:
        freq = {}
        left, res = 0,0
        for i in range(len(s)):
            if s[i] not in freq: 
                freq[s[i]] = 1
            else: 
                freq[s[i]] += 1
            while len(freq) > K: 
                freq[s[left]] -= 1
                if freq[s[left]] == 0: 
                    del freq[s[left]]
                left += 1
            res = max(i-left+1, res)
        return res