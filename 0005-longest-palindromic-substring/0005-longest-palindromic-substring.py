class Solution:
    '''
        Version: 2
        Idea:
            Normal algorithm
            Instead of checking if all cases are palindrome 
            We check all CENTERS what is the longest palin they can expand to
        Complexity:
            - Time O(n^2): since we have n centers * n linear to check palin
    '''
    def longestPalindrome(self, s: str) -> str:
        best_l, best_r = 0, 1
        
        def expand_palin(l, r):
            while l - 1 >= 0 and r + 1 <= len(s) and s[l-1] == s[r]:
                l -= 1
                r += 1
            
            return l, r
              
        
        for i in range(1, len(s)):
            
            # even center
            if s[i-1] == s[i]:
                l,r = expand_palin(i-1, i + 1)
                if (r-l) > (best_r - best_l): best_l, best_r = l, r
            
            # odd center
            l, r = expand_palin(i, i + 1)
            if (r-l) > (best_r - best_l): best_l, best_r = l, r
            
        
        return s[best_l: best_r]
                