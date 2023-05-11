class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = [None] * len(nums)
        def rob_backward(end):
            if end < 0: return 0
            
            if memoize[end] is None:
                memoize[end] = max(
                    rob_backward(end - 2) + nums[end],
                    rob_backward(end - 1)
                )
            
            return memoize[end]
        
        return rob_backward(len(nums) - 1)