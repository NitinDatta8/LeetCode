class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque(maxlen=size)
        
    def next(self, val: int) -> float:
        q = self.queue
        q.append(val)
        return float(sum(q)/len(q))
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)