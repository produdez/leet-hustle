class Solution:
    '''
        Version: 2
            Bottom up backtracking with O(1) space
        Idea:
            Every case can be split 1 char or 2 char
            So check all cases (n^2)
            But since there's repeated work, we use memoize
        Complexity: 
        - Time: O(n) - reduced from O(n^2) of backtracking
        - Space: O(1) - result of decoding at each index is saved
    '''
    def numDecodings(self, s: str) -> int:
        # this is for idx len(s - 1) and len(s)
        nxt = [0,1] if s[-1] == '0' else [1,1]
        
        def countDecRev(start):
            if start < 0: return nxt[0]
            
            if s[start] == '0': total = 0
            else:
                total = nxt[0]
                if s[start] == '1' or \
                    (s[start] == '2' and s[start+1] in '0123456'):
                    total += nxt[1]
            
            nxt[0], nxt[1] = total, nxt[0]
            return countDecRev(start - 1)
            
        return countDecRev(len(s) - 2)
        