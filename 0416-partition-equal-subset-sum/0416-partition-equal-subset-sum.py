class Solution:
    '''
        Continue: bottom up approach and complexity
    '''
    def canPartition(self, nums: List[int]) -> bool:
        
        memoize = {}
        
        def validPartition(i, target):
            if i >= len(nums): return False
            if (i, target) in memoize: return memoize[i,target]
            if nums[i] == target: result = True
            else:
                result = (
                    validPartition(i + 1, target) or
                    validPartition(i + 1, target - nums[i])
                )
            
            memoize[i, target] = result
            return result
        
        
        total = sum(nums)
        if total % 2 != 0: return False 
        return validPartition(0, total // 2)