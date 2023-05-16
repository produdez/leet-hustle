class Solution:
    '''
        Version: 1
            DP with trick
        Idea:
            Since we cannot rob the first and the last house at the same time
            We just compare the two cases
            - Rob all except first
            - Rob all except last
            And see which one is better
            Cause it's very hard to keep track if we took the first house or not
            so we just split it into two separated cases.
        Complex: 
        - Time: O(2n) = O(n)
        - Space: O(1)
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def rob_non_cyclic(start, end):
            before, prev = 0, 0
            for i in range(start, end):
                before, prev = prev, max(before + nums[i], prev)
            return prev
        
        return max(
            rob_non_cyclic(0, len(nums) - 1),
            rob_non_cyclic(1, len(nums))
        )