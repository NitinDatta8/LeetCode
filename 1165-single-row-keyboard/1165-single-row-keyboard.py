class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        freq = {}
        for j,i in enumerate(keyboard): 
            freq[i] = j
        score,j = 0,0
        for i in word: 
            val = abs(freq[i] - j)
            j = freq[i]
            score += val 
        return score