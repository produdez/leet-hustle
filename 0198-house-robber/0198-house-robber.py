class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = [None] * len(nums)
        def rob_from(start):
            if start >= len(nums): return 0
            
            if memoize[start] is None:
                memoize[start] = max(
                    rob_from(start + 2) + nums[start],
                    rob_from(start + 1)
                )
            
            return memoize[start]
        
        return rob_from(0)