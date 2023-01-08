class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Version 2:
                - Get MulLeft O(n) 
                - And MulRight O(n)
                - And then construct MulExept O(n)
            Time: -> O(3n) -> O(n)
            Storage: O(3n) -> O(n)
        '''
        left = [1]
        right = [1]
        
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i-1])
            right.append(right[-1] * nums[(len(nums)-1)-(i-1)])

        return [left[i] * right[len(nums)-i-1] for i in range(len(nums))]