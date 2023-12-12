class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # optimal?
        
        m, n = (m,n) if m<n else (n,m)
        memoize = [1] * n
        diff = n-m
        for i in range(m-2, -1, -1): 
            memoize[i+diff] =  memoize[i+diff] * 2
            for j in range(i+diff-1, -1, -1):
                memoize[j] = memoize[j] + memoize[j+1]
        return memoize[0]