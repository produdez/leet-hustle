class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            if height[l] > height[r]:
                max_area = max(max_area, (r-l) * height[r])
                r -= 1
            elif height[l] < height[r]:
                max_area = max(max_area, (r-l) * height[l])
                l += 1
            else:
                max_area = max(max_area, (r-l) * height[l])
                l += 1
                r -= 1
            
        return max_area