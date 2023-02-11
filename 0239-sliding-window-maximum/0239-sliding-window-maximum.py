class Solution:
    '''
        Version 1.9:
            1. Using python lib to simulate the queue (double ended queue)
            2. Use a trick to not have to write two loops
        Idea:
            Same as version 1
            but use python lib
        Complexity: 
            - Time: O(n)
            - Space: O(k)
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque([]) # de.que = double ended queue
        left = 0
        result = []
        for right in range(len(nums)):
            while queue and nums[right] > queue[-1]:
                queue.pop()
            queue.append(nums[right])

            # Trick here, window is only valid when right+1 > k
            if right + 1 >= k:
                result.append(queue[0])
                
                if nums[left] == queue[0]: queue.popleft()
                left += 1
        return result