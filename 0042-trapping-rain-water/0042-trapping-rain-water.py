class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            Version 2:
                Optimal: Neetcode
                NOTE: if want simpler code to understand view a few commits before this
                (not version 1 tho, that's a different version)
            Complexity:
            - Time: O(n)
            - Space: O(1)
            
            Idea: 
                Notice that the water that can be trapped at every column is
                    min(maxLeft, maxRight) - height if > 0 else 0
                So we keep a left pointer and right pointer to track maxLeft and maxRight
                At every ilteration, we calculate the watter trap next to the smaller max
                Meaning:
                    - if maxLeft < maxRight -> calculate at idx left + 1
                    - if maxRight < maxLeft -> calculate at idx right - 1
                Why?
                    Because when one max is smaller, the equation min(maxLeft, maxRight)
                    equals that max
                    -> and that is the value for column at location next to that smaller max
            Note:
                There are some tricks in the code
                1. Increase left/right index instead of calculate current location
                    curr = left + 1 or right - 1
                2. By updating the max before updating the water, it is made 
                    sure that the trapped value is never negative
                    if curr.h < maxH then after update maxH = oldMaxH -> positive
                    if curr.h > maxH then after update maxH = curr.h -> zero
                
        '''
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        water = 0
        
        while left < right: # means there's a gap between (min size 3)
            if maxLeft <= maxRight:
                left += 1 # curr = left + 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
            else:
                right -= 1 # curr = right - 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
        return water