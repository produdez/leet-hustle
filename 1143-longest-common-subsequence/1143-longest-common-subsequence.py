class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memoize = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    memoize[i][j] = memoize[i+1][j+1] + 1
                else:
                    memoize[i][j] = max(memoize[i+1][j], memoize[i][j+1]) 
        
        return memoize[0][0]