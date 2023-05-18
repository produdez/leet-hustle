class Solution:
    '''
        Version: 1
        Idea: Dynamic Programming
            Where if P(left, right) is Palin then P(left-1, right-1) is
            also palin if s[left] == s[right]
        
        Complexity:
        - Time: O(n^2)
        - Space: O(n^2)
        Note: very slow, barely passes
    '''
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        memoize = {}
        memoize[(0,0)] = True
        
        m_left, m_right = 0, 0

        for i in range(1, len(s)):
            memoize[(i,i)] = True
            if s[i] == s[i-1]: 
                memoize[(i-1, i)] = True
                m_left, m_right = i-1, i
        
        for l in range(3, len(s) + 1):
            for i in range(0, len(s) - l + 1):
                left, right = i, i+l-1
                if memoize.get((left+1, right-1), False) and s[left] == s[right]:
                    memoize[(left,right)] = True
                    if l > m_right - m_left + 1:
                        m_left, m_right = left, right

        return s[m_left: m_right + 1]