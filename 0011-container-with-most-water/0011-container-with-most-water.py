class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            # print(l, r, height[l] ,height[r])
            w = (r-l)
            if height[l] > height[r]:
                min_h = height[r]
                r -= 1
            elif height[l] < height[r]:
                min_h = height[l]
                l += 1
            else:
                min_h =  height[l]
                l += 1
                r -= 1
            max_area = max(max_area, w*min_h)
            # print(min_h, w, max_area)
        return max_area