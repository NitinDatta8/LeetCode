class TimeMap:

    def __init__(self):
        self.freq = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
     
        self.freq[key].append([timestamp, value])
            

    def get(self, key: str, timestamp: int) -> str:
        res = self.freq[key]
        if res == []: 
            return ''
        s, e = 0, len(res) -1 

        while s <= e: 
            mid = (s + e) // 2
            if res[mid][0] > timestamp: 
                e = mid - 1
            else: 
                s = mid + 1
        if s == 0: 
            return ''
        else: 
            return res[s-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)