class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0
        water = 0
        while left < right - 1: # means there's a gap between
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            if maxLeft <= maxRight:
                smallerMax = maxLeft
                curr = left + 1
                left += 1
            else:
                smallerMax = maxRight
                curr = right - 1
                right -= 1
            water += max(0, smallerMax - height[curr])
            
        return water