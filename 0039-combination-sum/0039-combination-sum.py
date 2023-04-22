class Solution:
    '''
        Version: 2
            Binary dfs
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        comb, csum = [], 0
        def dfs(i):
            nonlocal csum
            if csum == target:
                results.append(comb.copy())
                return False
            
            if i >= len(candidates) or csum > target: 
                return False
            
            csum += candidates[i]
            if csum <= target:
                comb.append(candidates[i])
                dfs(i)
                csum -= comb.pop()
                dfs(i+1)
            else:
                csum -= candidates[i]
    
        dfs(0)
        return results 