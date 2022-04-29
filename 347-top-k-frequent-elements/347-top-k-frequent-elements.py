class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums: 
            freq[i] = 1 + freq.get(i,0)
        
        res = []
        freq = sorted(freq, key=freq.get, reverse=True)
        return freq[:k]