class TimeMap:
    '''
        Version: 1
        Note: 
            Binary search here
            1. Wants the max of the smaller value
            2. So I used the left pointer as the variable
        Idea:
            HashMap with 
            - Key: string
            - Value: Array of Tuple (timestamp, value)
            Binary search based on timestamp to get value
        Complexity:
        - set:
            - Time: O(1) unless when array need to be resized
            - Space: O(1) no extra space
        - get
            - Time: O(1) to get the array + O(log(n)) to search
                for value using timestamp
            - Space: O(1)
    '''
    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        if not arr or arr[0][0] > timestamp: return ""
        
        left, right = 0, len(arr) - 1
        while left < right:
            pivot = (left + right) // 2 + 1
            if arr[pivot][0] == timestamp: return arr[pivot][1]
            
            if timestamp > arr[pivot][0]:
                left = pivot
            else:
                right = pivot - 1

        return arr[left][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)