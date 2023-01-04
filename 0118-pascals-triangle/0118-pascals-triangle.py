class Solution:
    '''
        Idea: Dynamic programing
        Build the pyramid bottom up
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        pyramid = [[1]]
        if numRows == 1: return pyramid
        
        for rowNum in range(2, numRows + 1):
            row = [1] * rowNum
            for i in range(1, rowNum - 1): # skiping head and tail of the row
                prevRow = pyramid[rowNum - 2]
                row[i] = prevRow[i-1] + prevRow[i]
            pyramid.append(row)
        return pyramid