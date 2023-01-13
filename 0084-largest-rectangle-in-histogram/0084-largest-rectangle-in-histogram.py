class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [(0,0)]
        max_area = 0
        for index, new_height in enumerate(heights):
            left_expanded = index
            while stack[-1][1] > new_height:
                start_idx, height = stack.pop()
                area = height * (index - start_idx)
                max_area = max(max_area, area)
                left_expanded = start_idx
            stack.append((left_expanded, new_height))
        
        for start_idx, height in stack:
            area = (len(heights) - start_idx) * height
            max_area = max(max_area, area)
        return max_area

            