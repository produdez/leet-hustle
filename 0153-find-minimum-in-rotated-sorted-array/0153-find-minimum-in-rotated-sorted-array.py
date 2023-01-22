class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            Version 1
            
            Idea:
            1. No matter where you are on the circle, there's bound to be some one smaller than you on your left or right
            2. Check step very big and then smaller, smaller (div by 2)
                If you're a very big number, you'll quickly walk towards smaller
                If you're a small number, you'll wait until the steps are small enough for you to walk around
            3. At the end, exactly after log2(len) steps, you are bound to be
            at the minimum or next to it
                -> that's why result is min(pivot, pivot - 1)
                
            Complexity:
            - Time: O(log(n))
            - Space: O(1)
        '''
        pivot = len(nums) // 2
        i = len(nums) // 2
        
        while i > 0:
            left = (pivot - (1+i)) % len(nums)
            right = (pivot + (1+i)) % len(nums)
            if nums[right] < nums[pivot]: 
                pivot = right            
            elif nums[left] < nums[pivot]:
                pivot = left
                        
            i = i//2
            
        return min(nums[pivot], nums[pivot - 1])
                
        