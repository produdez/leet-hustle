class Solution:
    '''
        Version: 2
            Bottom Up DP
        Idea:
            Build up our wordBroken str from it's wordBroken substr
            from index n to index 0
            
            From right to left, check all words in dictionary
            memoize[i] = match and memoize[i: i + len(matching_word)] (at least 1)
        Complexity:
        - Time: O(N * NW * W): check all pos (n) for all words (WD) and each word
            comparison takes avg word size (W)
        - Space: O(n) memoize
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoize = [None] * (len(s) + 1)
        memoize[-1] = True
        
        def check(i):
            matched = False
            for word in wordDict:
                if s[i] == word[0] and s[i: i+len(word)] == word: 
                    matched = memoize[i + len(word)]
                    if matched: break
            memoize[i] = matched
        
        for i in reversed(range(0, len(s))):
            check(i)
        return memoize[0]