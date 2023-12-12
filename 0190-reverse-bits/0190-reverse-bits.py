class Solution:
    def reverseBits(self, n: int) -> int:
        # naive string approach
        binary = str(bin(n))[2:]
        rev = binary[::-1]
        return int(rev, base=2)  << (32 - len(binary))