class Solution:
    def trap(self, height: List[int]) -> int:   
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        water = 0
        
        while left < right - 1: # means there's a gap between (min size 3)
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
        return water