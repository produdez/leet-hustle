class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Version: 4
            
            Space - O(1): assuming sorting does not take time
            
        '''
        if len(t) != len(s): return False
        return sorted(s) == sorted(t)
        