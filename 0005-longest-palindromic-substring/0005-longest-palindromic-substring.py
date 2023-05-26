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
        
        def expand_palin(center_idx):
            if isinstance(center_idx, int):
                l, r = center_idx, center_idx + 1
            else:
                l, r = int(center_idx - 0.5), int(center_idx + 1.5)
                if s[l] != s[r-1]: return int(center_idx), int(center_idx)
            
            while l - 1 >= 0 and r + 1 <= len(s) and s[l-1] == s[r]:
                l -= 1
                r += 1
            
            return l, r
            
            
        
        for i in range(1, len(s)):
            l,r = expand_palin(i - 0.5)
            # print(f'best palin from {i-0.5} is {s[l:r]}')
            if (r-l) > (best_r - best_l): best_l, best_r = l, r
                
            l, r = expand_palin(i)
            # print(f'best palin from {i} is {s[l:r]}')
            if (r-l) > (best_r - best_l): best_l, best_r = l, r
            
        
        return s[best_l: best_r]
                