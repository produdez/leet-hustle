class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def setNegative(i,j, value=None):
            # set to -1
            matrix[i][j] = value   
            for k in range(len(matrix)):
                if matrix[k][j] == 0:
                    setNegative(k,j)
                matrix[k][j] = value
            for k in range(len(matrix[0])):
                if matrix[i][k] == 0:
                    setNegative(i,k)
                matrix[i][k] = value
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                if val != 0: continue
                setNegative(i,j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        
        return