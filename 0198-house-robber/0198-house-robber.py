class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = {}
        def rob_from(start):
            if start >= len(nums): return 0
            # print('idx: ', start)
            if start in memoize: 
                # print('memoized')
                return memoize[start]
            
            best = 0
            for idx in range(start, len(nums)):
                best = max(
                    best,
                    nums[idx] + rob_from(idx + 2)
                )
            
            memoize[start] = best
            return best
        rob_from(0)
        # print(memoize)
        return memoize[0]