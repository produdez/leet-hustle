class Solution:
    '''
        Version: 1
            Cached (Top down DP)
        Idea:
            check each word with the string and save result
            Meaning if s[start : len(s)] is valid/or invalid
            we'll save it and save the computation
        Complextiy:
        - Time: O(NW * W * N) 
            with NW: num_word, W: word_count, N: str_len
            If no caching then time is
            O(NW^n * M * N) with n aprox N and is depth of deci tree with
            branching factor NW
        - Space: O(n) memoize
    '''
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
                