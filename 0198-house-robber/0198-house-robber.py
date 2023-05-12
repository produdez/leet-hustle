class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for val in nums:
            temp = cur
            cur = max(cur, prev + val)
            prev = temp
        return cur