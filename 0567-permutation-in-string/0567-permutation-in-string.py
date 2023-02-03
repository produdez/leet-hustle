class Solution:
    '''
        Version: 2
        Idea:
        1. Use hash map to represent a substr's representation
        2. Preconstruc hash map for s1 and our moving window
            * Just update HashMap of window when it's shifted 
            (add 1 remove 1)
        Complexity:
        - Time: 
            Setup init hashMaps: O(2 * n1)
            Traverse the array: O(n2 - n1)
                Checking match O(1) (hashmap compare)
                Updating hash map when window shifted:
                    O(1) for adding and O(1) for removing
                    * Note it's armortized O(1)
            Total: O(2*n1) + O(n2 - n1) * (O(1) + O(1) + O(1))
            -> O(n2 - n1)
        - Space:
            We only need 2 maps of sized n1
            -> O(2 * n1) = O(n1)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        left, right = 0, len(s1) - 1
        
        # Contruct HashMaps
        dict_s1 = {}
        dict_window = {}
        for c in s1:
            dict_s1[c] = dict_s1.get(c, 0) + 1
        for c in s2[left: right + 1]:
            dict_window[c] = dict_window.get(c, 0) + 1
        
        # Ilterate and check
        while True:
            if dict_window == dict_s1: return True
            
            if dict_window[s2[left]] == 1: del dict_window[s2[left]]
            else: dict_window[s2[left]] -= 1

            left += 1
            right += 1
            if right >= len(s2): return False
            dict_window[s2[right]] = dict_window.get(s2[right], 0) + 1
                
                    
            