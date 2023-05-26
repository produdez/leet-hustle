class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 1 # s[0:1] is auto palin
        
        def expand_count(l, r):
            count = 1
            while l - 1 >= 0 and r + 1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
                count += 1
            
            return count
        
        for i in range(1, len(s)):
            
            if s[i-1] == s[i]: # even case
                l, r = i-1, i
                count += expand_count(l, r)

            
            # odd case
            l, r = i, i
            count += expand_count(l, r)
        return count