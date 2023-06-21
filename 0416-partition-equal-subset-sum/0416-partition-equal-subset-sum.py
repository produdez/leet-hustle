class Solution:
    '''
        Continue: bottom up approach and complexity
    '''
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1: return False
        queue = [(len(nums) - 1, total // 2)]
        memoize = set()
        
        while queue:
            i, target = queue.pop(0)
            if i < 0: continue
            if (i,target) in memoize: continue
            if target == nums[i]: return True
            
            memoize.add((i, target))
            queue.append((i-1, target))
            queue.append((i-1, target - nums[i]))
        
        return False
            
            