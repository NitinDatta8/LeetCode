class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        
    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums)%2==0: 
            median = (self.nums[len(self.nums)//2-1] + self.nums[len(self.nums)//2])/2
        else: 
            median = self.nums[len(self.nums)//2]
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()