class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoize = [None] * (len(s) + 1)
        memoize[-1] = True
        
        def check(i):
            matched = False
            for word in wordDict:
                if s[i] == word[0] and s[i: i+len(word)] == word: 
                    matched = memoize[i + len(word)]
                    if matched is True: break
            memoize[i] = matched
        
        for i in reversed(range(0, len(s))):
            check(i)
        return memoize[0]