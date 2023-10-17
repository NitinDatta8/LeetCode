class SnapshotArray:

    def __init__(self, length: int):
      
        self.ids = defaultdict(list)
        self.snap_index = 0

    def set(self, index: int, val: int) -> None:
        if self.ids[index] and self.ids[index][-1][0] == self.snap_index: 
            self.ids[index][-1][1] = val 
            return 
        self.ids[index].append([self.snap_index, val])

    def snap(self) -> int:
        self.snap_index += 1
        return self.snap_index - 1 

    def get(self, index: int, snap_id: int) -> int:
        arr = self.ids[index]  
        s, e = 0, len(arr) - 1
        ans = -1
        while s <= e: 
            mid = (s + e) // 2
            if arr[mid][0] <= snap_id: 
                ans = mid
                s = mid + 1
            else: 
                e = mid - 1
        if ans == -1: 
            return 0 
        return arr[ans][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)