class NumArray:

    def __init__(self, nums: List[int]):
        self.accu = nums
        for i in range(1,len(nums)):
            self.accu[i] += self.accu[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.accu[right] - (self.accu[left-1] if left>0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)