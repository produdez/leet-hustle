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
        
        for i in range(1, len(stack)):
            i1,h1,s1 = stack[i]
            i0,h0,s0 = stack[i-1]
            water += h1 * (i1 - i0 - 1) - s1
            
        return water