class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        freq = {}
        freq1 = {}
        pattern = list(pattern)
        s = s.split(" ")
        if len(s)!=len(pattern):
            return False
        for word,p in zip(s,pattern): 
            if p not in freq: 
                freq[p] = word
            else:
                if freq[p]!=word:
                    return False
            if word not in freq1: 
                freq1[word] = p 
            else: 
                if freq1[word]!=p:
                    return False
        return True