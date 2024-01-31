class Solution:
    def hammingWeight(self, n: int) -> int:
        """
            Trick explain:
            1. n-1 will subtract one bit from n
            2. n & (n-1) will unset the next valid bit
            Example:
            n   : 101000
            n-1 : 100111
            n & (n-1)
            =   : 100000 (valid bit was remove)
            
            Complexity: O(32) aka O(1) since max size of num is 32 bit
            But we actually iterate only the valid bit so there's best case and avg case
        """
        count = 0
        while n:
            count += 1
            n = n & (n-1) # TRICK
            
        return count