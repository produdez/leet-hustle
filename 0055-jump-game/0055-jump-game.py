class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canEnd = [False] * n
        canEnd[-1] = True
        
        for i in reversed(range(n-1)):
            if nums[i] > n - i - 1:
                canEnd[i] = True
                continue
            for jump in range(1, nums[i] + 1):
                if canEnd[i + jump]:
                    canEnd[i] = True
                    break
        return canEnd[0]