class Solution:
    def reverseBits(self, n: int) -> int:
        # naive string manip
        
        binary = str(bin(n))[2:]
        padded = ('0' * (32 - len(binary))) + binary
        rev = padded[::-1]
        return int(rev, base=2)