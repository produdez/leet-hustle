class Solution:
    '''
        Version: 2
            Memoized Bottom up
        Idea:
            So u can climb 1 step or 2 steps
            Meaning ways to climb n steps
            = ways(n-1) # means try climb 1 step and climb the rest 
            + ways(n-2) # means try climb 2 step and climb the rest
            => This creates a tree with many repeated steps
    '''
    def climbStairs(self, n: int) -> int: 
        if n == 1: return 1
        ways = [1,2]
        for i in range(2, n):
            ways.append(ways[i-1] + ways[i-2])
        return ways[n-1]