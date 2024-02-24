class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if len(nums) < k:
            self.heap = nums
        else:
            nums.sort(reverse=True) # O(nlogn)
            self.heap = nums[:k]
            
        heapq.heapify(self.heap) # O(k)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val) 
        else:
            heapq.heappush(self.heap, val)
        
        # nlog(n)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)