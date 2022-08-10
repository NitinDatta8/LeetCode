class Solution:
    def numSplits(self, s: str) -> int:
        l = collections.Counter()
        r = collections.Counter(s)
        count = 0
        for c in s: 
            l[c] += 1
            r[c] -= 1
            if r[c] == 0: 
                del r[c]
            
            if len(l) == len(r): 
                count += 1
        return count