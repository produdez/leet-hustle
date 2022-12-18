class Solution:
    def maxArea(self, heightList: List[int]) -> int:
        '''
        Version 1.0

        Intuition:
            1. Start from outside in (meaning reducing the width slowly)
            2. Given a left_bar and a right_bar (a lower, a larger),
                - since width is max (we go outside in)
                - current area <= area(larger, next_inner_height)
                - meaning we skip checking the smaller bar
                And if lower = larger, we skip both current left and right
                    since no way there's a combination of either of them with an inner one that's bigger.
        '''
        leftIdx = 0
        rightIdx = len(heightList) - 1
        
        largestArea = 0
        while True:
            width = rightIdx - leftIdx
            if width <= 0: break

            leftH, rightH = heightList[leftIdx], heightList[rightIdx]
            height = min(leftH, rightH)
            largestArea = max(width * height, largestArea)
            
            if height == leftH: leftIdx += 1
            if height == rightH: rightIdx -= 1
        
        return largestArea 

