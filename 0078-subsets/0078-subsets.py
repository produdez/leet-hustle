class Solution:
    '''
        Version 3:
            DFS using index to save space
        
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        cur_set = []
        def dfs(num_idx):
            if num_idx >= len(nums): # done
                result.append(cur_set.copy())
                return
            
            # add
            cur_set.append(nums[num_idx])
            dfs(num_idx+1)
            
            # not add
            cur_set.pop()
            dfs(num_idx+1)
        
        dfs(0)
        return result