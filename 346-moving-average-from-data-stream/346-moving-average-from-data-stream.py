class MovingAverage:

    def __init__(self, size: int):
        self.window = size 
        self.count = 0 
        self.list = []
        
    def next(self, val: int) -> float:
        average = 0
        self.list.append(val)
        self.count+= 1
        if self.count <= self.window:  
            average = sum(self.list[-self.window:])/self.count
        else:
            average = sum(self.list[-self.window:])/self.window
        return average
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)