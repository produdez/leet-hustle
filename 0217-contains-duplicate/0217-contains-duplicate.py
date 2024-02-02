class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = set()
        for num in nums:
            if num in uniq: return True
            uniq.add(num)
        return False