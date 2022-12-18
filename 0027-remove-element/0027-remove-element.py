class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for v in nums:
            if v == val: continue
            
            nums[k] = v
            k += 1
        return k