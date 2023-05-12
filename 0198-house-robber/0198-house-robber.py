class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        prev, cur = nums[0], max(nums[0],nums[1])
        for i in range(2, len(nums)):
            print(prev,cur)
            temp = cur
            cur = max(
                cur,
                prev + nums[i]
            )
            prev = temp
        # print(prev, cur)
        return cur