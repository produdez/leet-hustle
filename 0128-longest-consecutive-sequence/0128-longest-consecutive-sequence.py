class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Version 2: Similar but easier to understand
            
            Idea:
                1. convert our list to a set for easy lookup
                2. Ilterate until hit a head of a sequence 
                    -> then build sequence and update longest
        '''
        if not nums: return 0
        nums = set(nums)
        
        longest = 0        
        for num in nums:
            if num - 1 not in nums: # sequence head
                streak = 1
                val = num
                while val + 1 in nums:
                    val += 1
                    streak += 1
                longest = max(longest, streak)
        return longest
            
            
        