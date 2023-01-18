class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            Version 1:
            
            Idea:
            - Keep monotonic-decresing stack ordered by height
            - Each node keeps track of it's sunken value, which includes
                - smaller nodes that comes before it
                - and water trapped that's already calculated
            - So we keep adding node to the stack if height is larger, else:
                1. Calculate trapped water (note to subtract sunken of current node and sunken of the last node in stack)
                2. Update total water and sunken stuffs
                3. Repeat until the stack is decreasing again
            - Lastly we go through the stack once more to add the water trapped between
            the remaining ones
            
            NOTE: why decreasing stack ?
                Cus we can only calculate sunken bottom up
        '''
        stack = [] # (index, height, sunken) , ordered decreasingly by height
        water = 0

        for i, h in enumerate(height):
            sunken = 0
            while stack and h >= stack[-1][1]:
                prev_i, prev_h, prev_sunken = stack.pop()
                trapped = (i - prev_i - 1) * prev_h - sunken
                water += trapped
                sunken += trapped + prev_h + prev_sunken
            stack.append((i,h,sunken))
        
        while len(stack) >= 2:
            i, h, sunken = stack.pop()
            water += h * (i - stack[-1][0] - 1) - sunken
            
        return water