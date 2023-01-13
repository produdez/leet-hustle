class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
            Version 1 (I dint solve this myself)
            
            Idea: Calculate the area that each block (each height) can expand to
            - Keep a monotonic inceasing stack of (start_index, height)
            - start_index is the left-most index that "height" can expand to
            
            Every time new height is checked (abbreviate 'top' as stack.top)
            - If height > top.height 
                -> cant expand left -> push (curr_idx, height)
            - Else: this means that top cant expand right anymore, so
                1. We calculate top's area -> update max area
                2. We update the index of current height
                    (Cause height < top.height so it can expand left to top.index)
                3. Repeat until the whole stack is monotonic again
            Lastly, after loop, pop all remaining stack elements and update max_area
            
            Complexity:
            - Time: O(2n) cause every env is pushed and poped once
            - Space: O(n+1) worse case all monotonic
                +1 cause I added extra entry
            Notes/tricks:
            - Start the stack with (0,0) to never encounter empty stack edge case
            - Note the width calculation in line #! 1
            - Also note that when a rec is poped, the current rec appends to the
                poped rec's start_index, not just index-1
        '''
        stack = [(0,0)]
        max_area = 0
        for index, new_height in enumerate(heights):
            expanded_index = index
            while stack[-1][1] > new_height:
                start_idx, height = stack.pop()
                area = height * (index - start_idx) #! 1
                max_area = max(max_area, area)
                expanded_index = start_idx

            stack.append((expanded_index, new_height))
        
        for start_idx, height in stack:
            area = (len(heights) - start_idx) * height
            max_area = max(max_area, area)
        return max_area

            