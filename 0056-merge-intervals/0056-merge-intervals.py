from itertools import takewhile

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        
        res = []
        cur = intervals[0]
        
        for nxt in intervals[1:]:
            if cur[1] < nxt[0]:
                res.append(cur)
                cur = nxt
            else:  
                cur = [
                    min(cur[0], nxt[0]),
                    max(cur[1], nxt[1])
                ]
                
        res.append(cur)
        return res