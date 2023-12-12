class Solution:
    def reverseBits(self, n: int) -> int:
        # math solution (iterate + add padding)
        
        if n == 0: return 0
        bit_count = int(math.log2(n)) + 1
        res = 0
        while n > 0:
            res = res << 1
            res += n % 2
            n = n >> 1
        return res << (32 - bit_count)