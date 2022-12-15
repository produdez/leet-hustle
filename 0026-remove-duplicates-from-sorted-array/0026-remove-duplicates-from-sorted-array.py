class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(i,j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            
        unique = nums[0]
        unq_count = 1
        duplicated = 0
        for i in range(1, len(nums)):
            val = nums[i]
            if val != unique:
                if i > unq_count - 1:
                    swap(i, unq_count)
                    
                unique = val
                unq_count += 1
        return unq_count
