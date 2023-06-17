class Solution:
    '''
        Version: 1
            Recursive DFS with caching for armotized complexity
            Basically topdown dynamic cheat
        Idea:
            1. Base idea is you find subset that sums to half of the original
                subset
            2. And you keep track by the starting index of subset and target 
                that you're summing to
            
            CHEAT: use caching
            1. Basically, dfs will check all combination, meaning for each element
                we have 2 choice: include/disclude -> O(2^n) time complex
            2. But, when using cache, the complexity reduces to the complexity of
                the cache. 
            3. And since the cache made up from (index, target) which has complex
                O(n * sum(nums))
                This caps the complextity down to O(n * sum(nums))
            4. And given the constrait that nums.length >> nums[i]
                Meaning 2^n >>>>>> O(n*sum(nums))
            We get a comparable result @@
            
            Complexity:
            - Time: O(n * sum(nums))
            - Space: Same
    '''
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