class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Version 1: 99% fastest
            
            Idea:
                1. convert our list to a set for easy lookup
                2. Ilterate while popping our set till empty
                    - get a value
                    - keep expanding consecutive (head and tail) until unavailable
                    - Note to remove checked value out of set
                    - And update longest streak
            Complexity:
            - Time: O(n) - convert + O(n) to ilterate and pop all values to check streak
                -> O(n)
            - Space: O(n) to store the HashSet that we converted our list into
        '''
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
            
            
        