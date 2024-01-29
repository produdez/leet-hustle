class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        rows = [False] * n
        cols = [False] * m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(n):
            if not rows[i]: continue
            matrix[i] = [0] * m
        for j in range(m):
            if not cols[j]: continue
            for i in range(n):
                matrix[i][j] = 0
                

                
        