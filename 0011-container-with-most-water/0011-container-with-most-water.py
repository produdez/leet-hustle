class Solution:
    def maxArea(self, heightList: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(heightList) - 1
        
        largestArea = 0
        while rightIdx - leftIdx > 0:

            leftH, rightH = heightList[leftIdx], heightList[rightIdx]
            height = min(leftH, rightH)
            largestArea = max((rightIdx - leftIdx) * height, largestArea)
            
            if height == leftH: leftIdx += 1
            if height == rightH: rightIdx -= 1
        
        return largestArea 

