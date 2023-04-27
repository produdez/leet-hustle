class Solution:
    '''
        Version: 3
            Memoized Bottom up
            but optimized since we only need 2 variables to keep track
            of everything, no need for a gigantic array
        Idea:
            So u can climb 1 step or 2 steps
            Meaning ways to climb n steps
            = ways(n-1) # means try climb 1 step and climb the rest 
            + ways(n-2) # means try climb 2 step and climb the rest
            => This creates a tree with many repeated steps
    '''
    def climbStairs(self, n: int) -> int: 
        one, two = 1, 2
        for _ in range(n-1):
            temp = two
            two = one + two
            one = temp
        return one