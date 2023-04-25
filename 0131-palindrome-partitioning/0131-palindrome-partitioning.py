class Solution:
    '''
        Version: 2
            Backtrack split with index only not string slicing
    '''
    def partition(self, s: str) -> List[List[str]]:
        res = []
        splits = []

        def isPalin(start, end):
            for i in range(start, (start + end + 1) // 2):
                if s[i] != s[start + end - i]: return False
            return True
        
        def gen_splitted(splits):
            lst = [s[:splits[0]+1]]
            for i in range(1, len(splits)):
                lst.append(s[splits[i-1]+1 : splits[i] + 1])
            res.append(lst)
            
        def split(start=0):
            if start >= len(s):
                gen_splitted(splits)
                return

            for i in range(start, len(s)):
                if isPalin(start, i): 
                    splits.append(i)                    
                    split(i+1)
                    splits.pop()
                                
        # res = []
        # split()
        # for splits in split_cases:
        #     lst = [s[:splits[0]+1]]
        #     for i in range(1, len(splits)):
        #         lst.append(s[splits[i-1]+1 : splits[i] + 1])
        #     res.append(lst)
        split()
        return res
                
