class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = 0, len(matrix) * len(matrix[0]) - 1
        while True:
            pv = (left + right) // 2
            value = matrix[pv // len(matrix[0])][pv % len(matrix[0])]
            if target == value: return True
            
            if left == right == pv: break
            
            if target < value:
                right = pv
            else:
                left = pv + 1
        return False