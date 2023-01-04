from functools import reduce
class Solution:
    '''
        Current: more optimized naive build
    '''
        
    def generate(self, numRows: int) -> List[List[int]]:
        def genNextRow(prevRow):
            return [1] + [prevRow[i] + prevRow[i+1] for i in range(len(prevRow) - 1)] + [1]

        pyramid = [[1]]
        for _ in range(1, numRows):
            pyramid.append(genNextRow(pyramid[-1]))
        return pyramid