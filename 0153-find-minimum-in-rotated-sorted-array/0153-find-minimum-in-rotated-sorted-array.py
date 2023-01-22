class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = len(nums) // 2
        i = len(nums) // 2
        while True:
            left = (pivot - (1+i)) % len(nums)
            right = (pivot + (1+i)) % len(nums)
            if nums[right] < nums[pivot]: 
                pivot = right            
            elif nums[left] < nums[pivot]:
                pivot = left
            
            if i == 0: break
            
            i = i//2
            
        return min(nums[pivot], nums[pivot - 1])
                
        