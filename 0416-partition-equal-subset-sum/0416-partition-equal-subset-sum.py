class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memoize = {}
        
        def dfs(i, target):
            if i >= len(nums): return False
            if (i, target) in memoize: return memoize[(i, target)]
            
            res = nums[i] == target \
                or dfs(i + 1, target - nums[i]) \
                or dfs(i + 1, target)
            
            memoize[(i, target)] = res
            return res
        
        total = sum(nums)
        if total % 2 != 0: return False
        return dfs(0, total // 2)