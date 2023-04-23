class Solution:
    '''
        Version: 1
        Idea:
            Same as subsets
            but only allow use of duplicated element on one side of the tree
            to make sure no duplicated sets.
            
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            
            
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res
            
        