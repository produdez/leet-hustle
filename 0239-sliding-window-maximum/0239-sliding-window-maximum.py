class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = [nums[0]] # monotonic decreasing queue
        for num in nums[1: k]:
            while queue and num > queue[-1]: queue.pop()
            queue.append(num)
        
        left = 0
        result = [queue[0]]
        for right in range(k, len(nums)):
            if nums[left] == queue[0]: queue.pop(0)
            left += 1
            
            while queue and nums[right] > queue[-1]: 
                queue.pop()
            queue.append(nums[right])
            result.append(queue[0])
        return result