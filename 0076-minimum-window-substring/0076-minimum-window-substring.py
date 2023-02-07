class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        
        count_t = collections.defaultdict(int)
        for char in t:
            count_t[char] += 1
        
        count_w = collections.defaultdict(int)
        left = 0        
        to_match = len(count_t)
        match = 0
        best = ''
        for right in range(left, len(s)):
            count_w[s[right]] += 1

            if count_w[s[right]] == count_t[s[right]]: # match increases
                match += 1
            # trim
            while left < right and count_w[s[left]] - 1 >= count_t[s[left]]:
                count_w[s[left]] -= 1
                left += 1
            if match == to_match: # update
                best = s[left: right + 1] if len(best) == 0 or right + 1 - left < len(best) else best
                if left < right: # move left to update window
                    count_w[s[left]] -= 1
                    left += 1
                    match -= 1

        return best
                    
            