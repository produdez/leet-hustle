class Solution:
    '''
        Version 2: 
            Bottom up 1d optimized 1/0 knapsack
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