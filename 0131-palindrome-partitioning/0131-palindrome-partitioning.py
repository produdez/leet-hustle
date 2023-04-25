class Solution:
    '''
        Version: 1
            Naive backtrack with no optimization
                split and keep splitting
    '''
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - (i+1)]: return False
            return True

        def split(s, start=0):
            res = []
            for i in range(start, len(s)):
                head = s[: i+1]
                if isPalin(head): 
                    remain = s[i+1:]
                    if not remain: 
                        res.append([head])
                        break
                    remain_splits = split(remain)
                    for splits in remain_splits:
                        res.append([head] + splits)
                        
            return res
        
        return split(s)