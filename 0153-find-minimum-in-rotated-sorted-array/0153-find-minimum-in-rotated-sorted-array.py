class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = len(nums) // 2
        # print('nums: ', nums)
        i = len(nums) // 2
        while True:
            # print('------')
            # print('i: ', i, ' curr pivot: ', nums[pivot])
            left = (pivot - (1+i**2)) % len(nums)
            right = (pivot + (1+i**2)) % len(nums)
            
            if nums[right] < nums[pivot]: 
                pivot = right            
            elif nums[left] < nums[pivot]:
                pivot = left
            else:
                if i == 0: break
            
            # print(f'piv: {nums[pivot]}, left: {nums[left]}, right: {nums[right]}')
            i = i//2
            
        return nums[pivot]
                
        