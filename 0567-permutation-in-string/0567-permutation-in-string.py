class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        left, right = 0, len(s1) - 1
        
        dict_s1 = {}
        for c in s1:
            dict_s1[c] = dict_s1.get(c, 0) + 1
        dict_window = {}
        for c in s2[left: right + 1]:
            dict_window[c] = dict_window.get(c, 0) + 1
        
        while True:
            # print('window: ', s2[left: right + 1])
            # print('dw: ', dict_window)
            if dict_window == dict_s1: return True
            
            if dict_window[s2[left]] == 1: del dict_window[s2[left]]
            else: dict_window[s2[left]] -= 1
            left += 1
            right += 1
            if right >= len(s2): return False
            dict_window[s2[right]] = dict_window.get(s2[right], 0) + 1
                
                    
            