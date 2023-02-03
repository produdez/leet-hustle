class Solution:
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