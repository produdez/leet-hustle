class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canEnd = [False] * n
        canEnd[-1] = True
        
        for i in reversed(range(n-1)):
            maxJump = nums[i] if nums[i] < n - i - 1 else n - i - 1
            for jump in range(1, maxJump + 1):
                jumpTo = i + jump
                if canEnd[jumpTo]:
                    canEnd[i] = True
                    break
        return canEnd[0]