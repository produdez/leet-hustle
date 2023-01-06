class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Version: 2
            
            Idea:
                Build two dict and compare them
                
            Complexity:
                Compared with ver1, better time worse space
                But still same O(complexity)
            Time: 
                O(n) + O(1) since dict compare is O(1)
            Space:
                O(2n)
        '''
        if len(t) != len(s): return False
        
        ds, dt = {}, {}
        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
            
        return ds == dt
        