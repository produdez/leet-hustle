class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self._add(num)

    def _add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val) 
        else:
            heapq.heappush(self.heap, val)
    
    def add(self, val: int) -> int:
        self._add(val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)