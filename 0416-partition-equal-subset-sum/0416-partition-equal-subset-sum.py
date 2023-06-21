class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        
        halfSum = total // 2
        targets = {0}
        
        for num in nums:
            newTargets = []
            for target in targets:
                if target + num == halfSum: return True
                newTargets.append(target + num)
            targets.update(newTargets)
        return False