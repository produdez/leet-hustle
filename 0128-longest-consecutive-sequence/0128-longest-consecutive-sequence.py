class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        
        longest = 0        
        while nums:
            val = nums.pop()
            head = val + 1
            tail = val - 1
            streak = 1
            while head in nums:
                nums.remove(head)
                head += 1
                streak += 1
            while tail in nums:
                nums.remove(tail)
                tail -= 1
                streak += 1
            longest = max(longest, streak)
        return longest
            
            
        