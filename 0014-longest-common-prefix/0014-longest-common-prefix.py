class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def firstMismatchIndex(strs):
            index = 0
            try:
                while True:
                    char = strs[0][index]
                    for s in strs:
                        if s[index] != char: return index
                    index += 1
            except IndexError:
                return index
            
        return strs[0][0 : firstMismatchIndex(strs)]