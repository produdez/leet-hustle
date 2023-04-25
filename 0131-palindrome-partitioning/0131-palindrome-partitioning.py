class Solution:
    '''
        Version: 3
            More optimization with a shared split representation
            and result appended when found
            -> less passing params around
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
        
        # def gen_splitted(splits):
        #     lst = [s[:splits[0]+1]]
        #     for i in range(1, len(splits)):
        #         lst.append(s[splits[i-1]+1 : splits[i] + 1])
        #     res.append(lst)
            
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
                
