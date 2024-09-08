class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        first_row = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        first_row = 0
                    else:
                        matrix[i][0] = 0

        # Iterate the inner of the matrix as not to override the first row
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # remaining first row, col
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0