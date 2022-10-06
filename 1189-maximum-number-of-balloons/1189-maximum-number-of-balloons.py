'''
balloon

'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # text = collections.Counter(text)
        
        c = collections.Counter(text)
        return min(c["b"], c["a"], c["l"]//2, c["o"]//2, c["n"])