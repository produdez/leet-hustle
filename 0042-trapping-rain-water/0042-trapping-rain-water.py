# class Column:
    # def __init__(self, index, height, sunken_weight=0):
    #     self.index = index
    #     self.height = height
    #     self.sunken_weight = sunken_weight

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [(-1,0,0)] # index, height, sunken
        water = 0
        # print(stack, 'water: ', water)
        for i, h in enumerate(height):
            # print('-------')
            # print('new: ', (i,h))
            if h < stack[-1][1]:
                stack.append((i,h,0))
            else:
                sunken = 0
                while stack and stack[-1][1] <= h:
                    prev_i, prev_h, prev_sunken = stack.pop()
                    full_h = (i - prev_i - 1) * prev_h
                    # print('full: ', full_h)
                    increment = max(0, full_h - sunken)
                    water += increment
                    sunken += increment + prev_h + prev_sunken
                    # print('i,h,inc,sunc,water: ', prev_i, prev_h, increment, sunken, water)
                stack.append((i,h,sunken))
            
            
            # print(stack)
            # print('water: ', water)
        
        for i in range(1, len(stack)):
            i1,h1,s1 = stack[i]
            i0,h0,s0 = stack[i-1]
            water += h1 * (i1 - i0 - 1) - s1
            
        return water