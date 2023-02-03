class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        left, right = 0, len(s1)
        
        dict_s1 = collections.defaultdict(int)
        for c in s1:
            dict_s1[c] += 1
        
        while right < len(s2) + 1:
            if s2[left] in dict_s1:
                temp_left = left
                while temp_left < right:
                    if dict_s1[s2[temp_left]] == 0:
                        temp_left -= 1
                        while temp_left >= left:
                            dict_s1[s2[temp_left]] += 1
                            temp_left -= 1
                        break
                    
                    dict_s1[s2[temp_left]] -= 1
                    temp_left += 1
                if temp_left == right: return True
            left += 1
            right += 1
        return False
                
                    
            