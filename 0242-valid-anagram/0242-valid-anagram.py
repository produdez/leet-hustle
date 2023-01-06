class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Version: 3
            Cheat using counter
        '''
        if len(t) != len(s): return False
        return Counter(t) == Counter(s)
        