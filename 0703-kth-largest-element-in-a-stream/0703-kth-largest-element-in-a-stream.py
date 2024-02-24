class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if len(nums) < k:
            self.heap = nums
        else:
            nums.sort(reverse=True)
            self.heap = nums[:k]
            
        heapq.heapify(self.heap) # O(k)
        self.k = k

        # print(sorted(self.heap))
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: heapq.heappop(self.heap)
        # if len(self.heap) == self.k:
        #     print('ppop')
        #     heapq.heappushpop(self.heap, val) # nlog(n)
        # else:
        #     print('push')
        #     heapq.heappush(self.heap, val)
        # print(sorted(self.heap))
        # print('added: ',  val, f'- {self.k}-max: ', self.heap[0])
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)