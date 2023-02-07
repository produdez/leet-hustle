class Solution:
    '''
        Version: 1
        
        Idea: Moving window, that does 3 things:
            0. window start with size 0
            1. Expand to the right adding new char and update count dictionary
            2. Strink from the left and remove un-needed char (frequency > in count_t)
            3. After expand and strink, if match is equal -> update the best result
            We use a variable here to keep track of match count
            -> avoid dict compare which takes time

        Complexity: m = len(s), n = len(t)
        
        - Time:
            O(n): construct count for t
            O(m + m): window expand max n times and can be strunk down max ~n time
            -> O(2m) (since) (m>n) (m<n then our algo would stop already)
            -> O(m)
        - Space: O(26* 2) since have upper and lowercase -> O(1)
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        
        count_t = collections.defaultdict(int)
        for char in t:
            count_t[char] += 1
        
        
        count_w = collections.defaultdict(int)
        to_match = len(count_t) # need this because len(count_t) will inc (defaultdict)
        left = 0        
        match = 0
        best = ''
        for right in range(left, len(s)):
            # add and update match
            count_w[s[right]] += 1
            if count_w[s[right]] == count_t[s[right]]: match += 1
            
            # trim excess
            while left < right and count_w[s[left]] - 1 >= count_t[s[left]]:
                count_w[s[left]] -= 1
                left += 1
            
            # update if good
            if match == to_match: 
                best = s[left: right + 1] if len(best) == 0 or right + 1 - left < len(best) else best
                if left < right: # just need to move left once and trim clear the rest
                    count_w[s[left]] -= 1
                    left += 1
                    match -= 1

        return best
                    
            