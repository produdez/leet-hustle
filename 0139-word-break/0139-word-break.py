class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        vocab = collections.defaultdict(set)
        for word in wordDict:
            vocab[word[0]].add(word)
            
        memoize = [None] * (len(s) + 1)
        memoize[-1] = True
        
        def check(start):
            if memoize[start] is not None: return memoize[start]
            
            res = False
            if s[start] in vocab:
                for word in vocab[s[start]]:
                    if word == s[start: start + len(word)]:
                        if check(start + len(word)): 
                            res = True
                            break
            memoize[start] = res
            return res
        
        return check(0)
                