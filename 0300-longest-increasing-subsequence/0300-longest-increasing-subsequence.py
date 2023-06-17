class Solution:
    '''
        Version: 1
            DP bottom up
            -> Cleaned up code
        Idea:
            Build the sequences from the right to left
            each cell in memoize is maxLe of sequence starting with number
            at that index
        Complexity:
        - Time: O(n^2)
        - Space: O(n)
        Note:
            If not for dynamic, complexity would be O(2^n) cause for 
            each element we have two choice to check
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        memoize = [1] * len(nums)
        maxLen = 1
        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]: 
                    memoize[i] = max(memoize[i], memoize[j] + 1)
            maxLen = max(maxLen, memoize[i])
        return maxLen