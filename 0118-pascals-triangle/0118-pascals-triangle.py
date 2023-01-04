from functools import reduce
class Solution:
    '''
        Note: this problem is hacked by many people with hardcode, naive solution is already very good
        
        Current: more optimized using offset sum
    '''
        
    def generate(self, numRows: int) -> List[List[int]]:
        pyramid = [[1]]
        for _ in range(1, numRows):
            pyramid.append(list(map(
                lambda a,b: a + b,
                [0] + pyramid[-1],
                pyramid[-1] + [0]
            )))
        return pyramid