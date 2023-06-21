class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        
        halfSum = total // 2
        targets = {0}
        
        for num in nums:
            newTargets = []
            for target in targets:
                s = target + num
                if s == halfSum: return True
                if s < halfSum: newTargets.append(s)
            targets.update(newTargets)
        return False