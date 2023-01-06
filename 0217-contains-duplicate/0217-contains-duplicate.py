class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
            Idea: Set (dictionary hashing)
            Time: O(n), Space: O(n)
        '''
        duplicate_set = set()
        
        for num in nums:
            if num in duplicate_set: # O(1)
                return True
            duplicate_set.add(num)
        return False