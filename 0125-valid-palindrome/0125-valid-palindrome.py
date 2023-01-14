class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            NOTE: if wanna do alnum() by yourself, just do ascilookup
             ord(char) between ('a','z') and ('A','Z') and ('0','9')
        '''
        
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum(): 
                l += 1
                continue
            if not s[r].isalnum(): 
                r -= 1
                continue
            if s[l].lower() != s[r].lower(): return False

            l += 1
            r -= 1
        
        return True