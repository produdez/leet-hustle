class Solution:
    '''
        Version: 2.-1
            Binary dfs but less efficient + cleaner code
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
            comb.append(candidates[i])
            good = dfs(i)
            csum -= comb.pop()
            
            if good: dfs(i+1)
            return True
    
        dfs(0)
        return results 