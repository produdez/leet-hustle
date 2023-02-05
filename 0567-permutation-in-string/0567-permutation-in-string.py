class Solution:
    '''
        Version: 3
            Optimized (neetcode)
        Idea: Same as version 2
            But update so as to remove the cost of HashMap compare
        => How? By keeping an variable indicating match rate
            * Note when a char exit/enter the window, the match decrease/increase
            ONLY IF window have less (or eq) frequency of that char
            Could be confusing but
                "dict_window[s2[left]] <= dict_s1.get(s2[left],0)"
            just means window have less count of s2[left] than dict_s1
        Complexity:
        Time: O(n1 + (n2-n1))
        Space: O(2 * m) = O(2 * 26) = O(1)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        left, right = 0, len(s1) - 1
        
        # Populate Init HashMap
        dict_s1 = {}
        dict_window = {}
        for i in range(len(s1)):
            dict_s1[s1[i]] = dict_s1.get(s1[i], 0) + 1
            dict_window[s2[i]] = dict_window.get(s2[i], 0) + 1
        
        # Calc init match
        match = 0
        for c in dict_s1:
            match += min(dict_window.get(c,0), dict_s1[c])
            
        # Move and compare
        while True:
            if match == len(s1): return True
            if right + 1 >= len(s2): return False
            
            # Update match
            
            # take out
            if dict_window[s2[left]] <= dict_s1.get(s2[left],0): match -= 1
            dict_window[s2[left]] -= 1
            if dict_window[s2[left]] == 0: dict_window.pop(s2[left])
            
            left += 1
            right += 1
  
            # put in
            dict_window[s2[right]] = dict_window.get(s2[right], 0) + 1
            if dict_window[s2[right]] <= dict_s1.get(s2[right], 0): match += 1
        
        
        
        