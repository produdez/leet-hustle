class Solution:
    '''
        Version: 1.5
            Update: add base case of countDec(len(s)) == 1
            Backtracking with DP memoize
        Idea:
            Every case can be split 1 char or 2 char
            So check all cases (n^2)
            But since there's repeated work, we use memoize
        Complexity: 
        - Time: O(n) - reduced from O(n^2) of backtracking
        - Space: O(n) - result of decoding at each index is saved
    '''
    def numDecodings(self, s: str) -> int:
        memoize = {len(s): 1}
        
        def countDec(start):
            if start in memoize: return memoize[start]
            if start >= len(s) or s[start] == '0': total = 0
            else:
                total = countDec(start+1)
                if start + 1 < len(s) and \
                    (
                        s[start] == '1' or 
                        (s[start] == '2' and s[start+1] in '0123456')
                    ):
                    total += countDec(start+2)
            
            memoize[start] = total
            return total
        
        
        return countDec(0)
        