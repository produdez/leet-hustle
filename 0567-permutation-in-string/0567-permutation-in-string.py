class Solution:
    '''
        Version: 1
        
        Idea: 
        1. Have a window of size s1 slide through s2
            And check if window matches s1's permutation
        2. Check match using hash map of char occurance
        
        Complexity:
        - Time: O(n2 - n1) - window slide time
            * O(n1) - time to check HashMap match
            n1: len(s1), n2: len(s2)
            -> Total O(m * n) where m is str diff and n is len of window
        - Space: O(2 * n1)
            At all time we just need hash map of s1 and hash map of window
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        window = [0, len(s1)]
        dict_s1 = collections.defaultdict(int)
        for c in s1:
            dict_s1[c] += 1
        while window[1] <= len(s2):
            dict_window = collections.defaultdict(int)
            for c in s2[window[0]: window[1]]:
                dict_window[c] += 1
            if dict_window == dict_s1: return True
            window[0] += 1
            window[1] += 1
        return False