class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(s):
            if len(s) == 1: return True
            return s == s[::-1]
        def split(s, start=0):
            res = []
            for i in range(start, len(s)):
                head = s[: i+1]
                # print('head: ', head)
                if isPalin(head): 
                    # print('is palin')
                    remain = s[i+1:]
                    if not remain: 
                        res.append([head])
                        break
                    remain_splits = split(remain)
                    for splits in remain_splits:
                        res.append([head] + splits)
                        
            return res
        
        return split(s)