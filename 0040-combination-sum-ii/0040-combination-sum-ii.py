class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        nums = []
        csum = 0
        
        def dfs(i):
            nonlocal csum
            if csum == target: 
                res.append(nums[::])
                return False
            
            if i >= len(candidates) or csum > target:
                # csum + candidates[i] > target
                return False
            
            nums.append(candidates[i])
            csum += candidates[i]
            valid = dfs(i+1)
            csum -= nums.pop() # pop before trying stuffs  wrong
            if not valid: return True
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1)
            
            return True
        dfs(0)
        return res