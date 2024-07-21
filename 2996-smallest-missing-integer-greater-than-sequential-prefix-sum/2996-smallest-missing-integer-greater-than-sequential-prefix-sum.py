class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lsum = nums[0]
        end_idx = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i] - 1: break
            
            lsum += nums[i]
            end_idx = i

        missing = lsum
        pool = set(nums[end_idx:])
        while missing in pool: missing += 1
            
        return missing