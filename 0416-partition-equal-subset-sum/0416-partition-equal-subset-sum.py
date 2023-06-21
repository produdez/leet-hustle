class Solution:
    '''
        Version: 3
            Optimal set problem
            
        Idea:
            Find halfsum and generate all sets to check if sum to that
            Stop asap
        Complexity:
        - Time: O(n*sum(nums)) armotized
            Why? Technically it should be O(2^n) cause there are O(2^n) subsets
            But there are only at most sum(nums) distinct sums so it's reduced
            down to O(n * sum(nums))
            And it perform better than knapsack depending on the set distribution
        - Space: O(sum(nums))
    '''
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