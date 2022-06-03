class SparseVector:
    def __init__(self, nums: List[int]):
        self.hashmap = {}
        for i, val in enumerate(nums):
            if val != 0: 
                self.hashmap[i] = val 
            

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0 
        for k, v in vec.hashmap.items():
            if k in self.hashmap:
                res += v * self.hashmap[k]
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)