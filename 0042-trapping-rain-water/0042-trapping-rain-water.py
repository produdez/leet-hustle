# class Column:
    # def __init__(self, index, height, sunken_weight=0):
    #     self.index = index
    #     self.height = height
    #     self.sunken_weight = sunken_weight

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] 
        water = 0
        for i, h in enumerate(height):
            sunken = 0
            while stack and stack[-1][1] <= h:
                prev_i, prev_h, prev_sunken = stack.pop()
                full_h = (i - prev_i - 1) * prev_h
                increment = max(0, full_h - sunken)
                water += increment
                sunken += increment + prev_h + prev_sunken
            stack.append((i,h,sunken))
        
        while len(stack) >= 2:
            i, h, sunken = stack.pop()
            water += h * (i - stack[-1][0] - 1) - sunken
            
        return water