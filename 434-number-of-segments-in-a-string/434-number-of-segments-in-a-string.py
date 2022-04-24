class Solution:
    def countSegments(self, s: str) -> int:
        if s == "": return 0
        s = s.split(' ')
        res = []
        for i in s: 
            if i!='':
                res.append(i)
        return len(res)