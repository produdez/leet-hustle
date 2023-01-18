class Solution:
    def trap(self, height: List[int]) -> int:   
        left, right = 0, len(height) - 1
        maxLeft, maxRight, water = 0, 0, 0
        
        while left < right - 1: # means there's a gap between (min size 3)
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            
            if maxLeft <= maxRight:
                water += max(0, maxLeft - height[left + 1])
                left += 1
            else:
                water += max(0, maxRight - height[right - 1])
                right -= 1            
        return water