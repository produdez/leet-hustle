class Solution:
    '''
        Version: 1
            Memoized Recursion
        Idea:
            So u can climb 1 step or 2 steps
            Meaning ways to climb n steps
            = ways(n-1) # means try climb 1 step and climb the rest 
            + ways(n-2) # means try climb 2 step and climb the rest
            => This creates a tree with many repeated steps
    '''
    def climbStairs(self, n: int) -> int:        
        def recurClimb(n, ways):
            if n == 1: res = 1
            elif n == 2: res = 2
            else:
                if ways[n-1] is not None:
                    return ways[n-1]
                res = recurClimb(n-1, ways) + recurClimb(n-2, ways)

            ways[n-1] = res
            return res
        
        return recurClimb(n, [None] * n)