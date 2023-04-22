class Solution:
    '''
        Version: 2.-2
            Binary dfs even cleaner code with NO EARLY STOP
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        comb, csum = [], 0
        def dfs(i):
            nonlocal csum
            if csum == target:
                results.append(comb.copy())
                return
            
            if i >= len(candidates) or csum > target: return
            
            csum += candidates[i]
            comb.append(candidates[i])
            dfs(i)
            csum -= comb.pop()
            
            dfs(i+1)
    
        dfs(0)
        return results 