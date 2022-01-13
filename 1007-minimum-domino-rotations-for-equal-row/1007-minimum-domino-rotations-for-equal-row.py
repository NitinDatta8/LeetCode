class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_count = collections.Counter(tops)
        bottom_count = collections.Counter(bottoms)
        fin = top_count+bottom_count
        val = fin.most_common(1)[0][0]
        t,b = 0,0
        print(val)
        for i,j in zip(tops,bottoms):
            if i!=j:
                if i == val: 
                    t +=1 
                elif j == val:
                    b += 1
                else: 
                    return -1
            elif i==j and i!=val: 
                return -1
            
        print(t,b)
        return min(t,b)
        