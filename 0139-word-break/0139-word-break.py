class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:          
        memoize = [None] * (len(s) + 1)
        memoize[-1] = True
        
        def check(start):
            if memoize[start] is not None: return memoize[start]
            
            res = False
            for word in wordDict:
                if word == s[start: start + len(word)]:
                    if check(start + len(word)): 
                        res = True
                        break
            memoize[start] = res
            return res
        
        return check(0)
                