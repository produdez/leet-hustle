class Solution:
    def maxArea(self, heightList: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(heightList) - 1
        
        largestArea = 0
        while True:
            width = rightIdx - leftIdx
            if width <= 0: break

            leftH, rightH = heightList[leftIdx], heightList[rightIdx]
            height = min(leftH, rightH)
            largestArea = max(width * height, largestArea)
            
            if height == leftH:
                leftIdx += 1
            else:
                rightIdx -= 1
        
        return largestArea 

