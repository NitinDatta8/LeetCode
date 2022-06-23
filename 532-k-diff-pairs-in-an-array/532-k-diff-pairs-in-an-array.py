# 1 1 3 4 5 
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0 
        if k == 0: 
            for ke,v in c.items():
                if v>1: 
                    count += 1
        else: 
            for ke,v in c.items():
                if ke+k in c: 
                    count += 1
        return count