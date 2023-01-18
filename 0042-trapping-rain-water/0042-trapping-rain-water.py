class Solution:
    def trap(self, height: List[int]) -> int:   
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        water = 0
        
        while left < right - 1: # means there's a gap between (min size 3)
            if maxLeft <= maxRight:
                left += 1
                water += max(0, maxLeft - height[left])
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                water += max(0, maxRight - height[right])
                maxRight = max(maxRight, height[right])
        return water