class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[unq_count - 1]:
                if i > unq_count - 1: # means there's duplication
                    nums[unq_count] = nums[i]
                unq_count += 1
        return unq_count
