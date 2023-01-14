class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalpha() and not s[l].isnumeric(): 
                l += 1
                continue
            if not s[r].isalpha() and not s[r].isnumeric(): 
                r -= 1
                continue
            if s[l].lower() != s[r].lower(): return False

            l += 1
            r -= 1
        
        return True