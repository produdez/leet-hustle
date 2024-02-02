class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastValid = n - 1
        for i in reversed(range(lastValid)):
            if nums[i] >= lastValid - i:
                lastValid = i
        return lastValid == 0