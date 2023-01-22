class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            Version 3: Even better binary search
            
            
            Update:
                Instead of using a var, we use right to keep track of our valid result
                - And we make sure to stop when left == right
            Complexity:
            - Time: O(n + n * log(max(piles))) (init n to get max)
            - Space: O(1)
        '''
        
        l, r = 1, max(piles)
        
        def valid(speed):
            total = 0
            for p in piles:
                total += math.ceil(p/speed)
            return total <= h
        
        while l < r:
            piv = (l + r) // 2
            if valid(speed=piv): 
                r = piv
            else: 
                l = piv + 1
        return r
                
            