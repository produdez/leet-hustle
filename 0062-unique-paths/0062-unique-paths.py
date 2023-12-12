class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math solution
        # idea: (m-1 + n-1) boxes to put (m-1) of the first element and (n-1) of the second element
        # result? total way to arrange devide by duplicate
        # duplicate? well (m-1) of first and switch with each other ans same for second element
        # -> (m+n-2)! / (m-1)!(n-1)!
        # simplification -> (m+n-2)C(m-1) - (or Cn-1)
        
        return math.comb(m+n-2, m-1)