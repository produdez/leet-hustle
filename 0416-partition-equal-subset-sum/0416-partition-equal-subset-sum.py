class Solution:
    '''
        Version 2: 
            Bottom up 1d optimized 1/0 knapsack
        Idea:
            Build a 1d array representation of a 2d array for 1/0 knapsack
            array[i][j] means can i sum to target j with first i elements from nums
            array[i][j] = array[i-1][j] (sum to same target with less elem) 
                or array[i-1][j-nums[i]] (sum to target reduced by current element)
        Complexity:
        - Time: O(n * sum(nums))
        - Space: O(sum(nums)) or O(n * sum(nums)) if not optimized
    '''
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False

        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in reversed(range(target + 1)):
                if i - num >= 0: 
                    dp[i] = dp[i] or dp[i - num]
        return dp[target]