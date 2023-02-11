class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = [nums[0]]
        for num in nums[1: k]:
            while stack and num > stack[-1]: stack.pop()
            stack.append(num)
        
        left = 0
        result = [stack[0]]
        for right in range(k, len(nums)):
            if nums[left] == stack[0]: stack.pop(0)
            left += 1
            
            while stack and nums[right] > stack[-1]: 
                stack.pop()
            stack.append(nums[right])
            result.append(stack[0])
        return result