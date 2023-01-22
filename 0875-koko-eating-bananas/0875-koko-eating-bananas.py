class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            Version 2: Better binary search
            
            Update:
            1. use a variable to keep track of result instead of making
                the binary search complex
            2. always shift left or right away from current pivot so that our
                stopping condition is left > right
                
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
        
        result = r
        while l <= r:
            piv = (l + r) // 2
            if valid(speed=piv): 
                result = min(result, piv)
                r = piv - 1
            else: 
                l = piv + 1
        return result
                
            