class Solution:
    '''
        Version: 4
            path is the string splitted itself
            no need to record split index since its already in the dfs params
    '''
    def partition(self, s: str) -> List[List[str]]:
        res = []
        splits = []

        def isPalin(start, end):
            while start < end:
                if s[start] != s[end]: return False
                start += 1
                end -= 1
            return True
        
            
        def split(start=0):
            if start >= len(s):
                res.append(splits.copy())
                return

            for i in range(start, len(s)):
                if isPalin(start, i): 
                    splits.append(s[start: i+1])                    
                    split(i+1)
                    splits.pop()

        split()
        return res
                
