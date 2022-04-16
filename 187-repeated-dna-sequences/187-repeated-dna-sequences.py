class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq, res = set(), set()
        for l in range(len(s)-9):
            if s[l:l+10] not in freq:
                freq.add(s[l:l+10])
            else: 
                res.add(s[l:l+10])
        return list(res)