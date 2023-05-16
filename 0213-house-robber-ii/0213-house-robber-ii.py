class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob_non_cyclic(start, end):
            before, prev = 0, 0
            for val in nums[start: end]:
                before, prev = prev, max(before + val, prev)
            return prev
        
        return max(
            rob_non_cyclic(0, len(nums) - 1),
            rob_non_cyclic(1, len(nums))
        )