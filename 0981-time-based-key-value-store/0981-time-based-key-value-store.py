class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        if not arr or arr[0][0] > timestamp: return ""
        
        left, right = 0, len(arr) - 1
        
        res, ts_res = "", 0
        while left <= right:
            pivot = (left + right) // 2
            if arr[pivot][0] == timestamp: return arr[pivot][1]
            
            if timestamp > arr[pivot][0]:
                left = pivot + 1
                if ts_res < arr[pivot][0]:
                    ts_res, res = arr[pivot]
            else:
                right = pivot - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)