class Solution:
    '''
        Version: 2
            Backtrack split with index only not string slicing
    '''
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(start, end):
            for i in range(start, (start + end + 1) // 2):
                if s[i] != s[start + end - i]: return False
            return True

        def split(start=0):
            res = []
            for i in range(start, len(s)):
                if isPalin(start, i): 
                    remain = i+1
                    if remain >= len(s): 
                        res.append([i])
                        break
                    
                    remain_splits = split(remain)
                    for splits in remain_splits:
                        res.append([i] + splits)
                        
            return res
        
        res = []
        for splits in split():
            lst = [s[:splits[0]+1]]
            for i in range(1, len(splits)):
                lst.append(s[splits[i-1]+1 : splits[i] + 1])
            res.append(lst)
        return res
                
