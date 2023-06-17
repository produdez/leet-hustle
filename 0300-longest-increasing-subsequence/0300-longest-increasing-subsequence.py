class Solution:
    '''
        Version: 1
            DP bottom up
        Idea:
            Build the sequences from the right to left
            each cell in memoize is maxLe of sequence starting with number
            at that index
        Complexity:
        - Time: O(n^2)
        - Space: O(n)
    '''
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