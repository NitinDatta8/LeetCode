class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length+1)
        for s,e,inc in updates:
            res[s] += inc
            res[e+1]  -= inc
        for i in range(1,len(res)):
            res[i] += res[i-1]
        return res[:-1]