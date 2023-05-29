class Solution:
    '''
        Version: 1
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
        memoize = {}
        def valid(char):
            if not char or char[0] == '0': return False
            num = int(char)
            return num > 0 and num <= 26
        
        def countDec(start):
            if start in memoize: return memoize[start]
            
            if start == len(s):
                total = 1
            elif start < len(s):
                total = 0
                if valid(s[start]): total += countDec(start+1)
                if valid(s[start: start+2]): total += countDec(start+2)
            else:
                total = 0 
            
            memoize[start] = total
            return total
        
        
        return countDec(0)
        