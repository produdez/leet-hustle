class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = 0, len(matrix) * len(matrix[0]) - 1
        while True:
            pv = (left + right) // 2
            x = pv // len(matrix[0])
            y = pv % len(matrix[0])
            value = matrix[x][y]
            if target == value: return True
            
            if left == right == pv: break
            
            if target < value:
                right = pv
            else:
                left = pv + 1
        return False