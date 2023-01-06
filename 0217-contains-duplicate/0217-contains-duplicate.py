class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()
        
        for num in nums:
            if num in duplicate_set: # O(1)
                return True
            duplicate_set.add(num)
        return False