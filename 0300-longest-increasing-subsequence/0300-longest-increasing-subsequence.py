class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memoize = [0] * len(nums)
        maxLen = 0
        for i in reversed(range(len(nums))):
            l = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]: 
                    l = max(l, memoize[j] + 1)
            memoize[i] = l
            maxLen = max(l, maxLen)
        return maxLen