class SnapshotArray:

    def __init__(self, length: int):
        self.s_id = 0 
        self.freq = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        if self.freq[index] and self.freq[index][-1][1] == self.s_id: 
            self.freq[index][-1][0] = val 
            return 
        self.freq[index].append([val, self.s_id])


    def snap(self) -> int:
        self.s_id += 1
        return self.s_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.freq[index]
        s, e = 0, len(arr) - 1
        ans = -1
        while s <= e: 
            mid = (s + e) // 2
            if arr[mid][1] <= snap_id: 
                ans = arr[mid][0]
                s = mid + 1
            else: 
                e = mid - 1
        if ans == -1: 
            return 0 
        return ans


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)