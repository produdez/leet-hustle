class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def expand(nums, prev_sets=[[]]):
            if not nums: return prev_sets
            return expand(nums[1:], prev_sets + [s + [nums[0]] for s in prev_sets])
        
        return expand(nums)