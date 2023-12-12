class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bot = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        # Side: 0-top, 1-right, 2-bot, 3-left
        res = []
        while top <= bot and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1

            if top > bot or left > right: break
            
            for j in range(right, left -1 , -1):
                res.append(matrix[bot][j])
            bot -= 1
            for i in range(bot, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res