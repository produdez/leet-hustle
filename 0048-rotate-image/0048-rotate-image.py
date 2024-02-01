class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2): # there are n//2 layers size > 1
            for i in range(n - layer*2 -1): # each slice of a square is layer length - 1
                start,end = layer, n-layer-1
                temp = matrix[start][start+i]
                matrix[start][start+i] = matrix[end-i][start]
                matrix[end-i][start] = matrix[end][end-i]
                matrix[end][end-i] = matrix[start+i][end]
                matrix[start+i][end] = temp
        
        # inplace replace so no return