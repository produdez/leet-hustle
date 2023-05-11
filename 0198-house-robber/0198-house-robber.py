class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = {}
        def rob_from(start):
            if start >= len(nums): return 0
            if start in memoize: return memoize[start]
            
            best = 0
            for idx in range(start, len(nums)):
                best = max(
                    best,
                    nums[idx] + rob_from(idx + 2)
                )
            
            memoize[start] = best
            return best
        
        return rob_from(0)