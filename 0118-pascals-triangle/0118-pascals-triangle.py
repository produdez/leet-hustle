from functools import reduce
class Solution:
    '''
        Rerun!
        
        Current: more optimized naive build
    '''
        
    def generate(self, numRows: int) -> List[List[int]]:

        pyramid = [[1]]
        for lastRowIdx in range(0, numRows - 1):
            pyramid.append(
                [1] + 
                [pyramid[lastRowIdx][i] + pyramid[lastRowIdx][i+1] for i in range(lastRowIdx)] 
                + [1])
        return pyramid