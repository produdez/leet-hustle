class Solution:
    '''
        Version: 2
            N-ary dfs (simpler code)
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(pos, target, nums = []):
            if target == 0: res.append(nums.copy())
                
            if target <= 0: return False # done
            
            prev = -1 
            for i in range(pos, len(candidates)):
                if candidates[i] == prev: continue # exclude duplicates
                
                nums.append(candidates[i])
                valid = backtrack(i + 1, target - candidates[i], nums)
                nums.pop()
                
                if not valid: break
                prev = candidates[i]
            
            return True
        
        backtrack(0, target)
        return res
        