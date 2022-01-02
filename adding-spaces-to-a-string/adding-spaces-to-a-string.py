class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = ''
        cur = 0 
        for i,x in enumerate(s):
            if cur < len(spaces) and spaces[cur] == i: 
                new_s+=' '
                cur += 1
            new_s+= x
        return new_s