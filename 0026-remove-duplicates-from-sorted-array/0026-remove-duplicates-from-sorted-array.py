class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
            Solution:
            Read forward keeping a count of unique numbers
            If unq_count - 1 < current_index means there's a gap (duplication)
            so just overwrite the last duplicated index with the current new value
        '''
        unq_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[unq_count - 1]:
                if i > unq_count - 1: # means there's duplication
                    nums[unq_count] = nums[i]
                unq_count += 1
        return unq_count
