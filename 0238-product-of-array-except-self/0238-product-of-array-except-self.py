class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Version 2:
                - 
        '''
        left = [1]
        right = [1]
        
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i-1])
            right.append(right[-1] * nums[(len(nums)-1)-(i-1)])

        return [left[i] * right[len(nums)-i-1] for i in range(len(nums))]