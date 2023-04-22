class Solution:
    '''
        Version: 1
            My version of dfs, not very clean but efficient
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        vals, csum = [], 0
        
        
        def dfs(i):
            nonlocal csum
            if i >= len(candidates) or csum + candidates[i] > target:
                return False
            
            csum += candidates[i]
            
            vals.append(candidates[i])
            if csum == target: results.append(vals.copy())

            while dfs(i): i += 1 #early stop

            csum -= vals.pop()
            return True
        
        if target == 0: results.append([])
        for i in range(len(candidates)):
            dfs(i)
        return results 