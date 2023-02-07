class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        
        count_t = collections.defaultdict(int)
        for char in t:
            count_t[char] += 1
        
        count_w = collections.defaultdict(int)
        left, right = 0, 0
        count_w[s[left]] += 1
        
        # print('tomatch: ', count_t, '-len: ', len(count_t))
        to_match = len(count_t)
        match = 1 if count_w[s[left]] == count_t[s[left]] else 0
        if match == len(count_t): return s[0]
        best = ''
        # print('init: ', s[left:right+1], '-match', match)
        while True:
            if right + 1 < len(s):
                right += 1
                count_w[s[right]] += 1
                
                if count_w[s[right]] == count_t[s[right]]: # match increases
                    match += 1
                # print(f'left: {left}, right: {right}, str: {s[left:right+1]}, match: {match}')
                # trim
                while left < right and count_w[s[left]] - 1 >= count_t[s[left]]:
                    count_w[s[left]] -= 1
                    # if count_w[s[left]] == 0: count_w.pop(s[left]) # no need to pop
                    left += 1
                if match == to_match: # update
                    best = s[left: right + 1] if len(best) == 0 or right + 1 - left < len(best) else best
                    if left < right: # move left to update window
                        count_w[s[left]] -= 1
                        left += 1
                        match -= 1
                # elif count_w[s[right]] > count_t[s[right]]: # un-needed, could try to trim

            else:
                return best
                    
            