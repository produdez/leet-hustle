class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
            Implement 2's complement sum
        '''
        
        def calc(a,b,c):
            carry = (a and b) or (a and c) or (b and c)
            value = (a and b and c) or (not carry and (a or b or c))
            return value, carry
        
        BIT_COUNT = 10

        i,j,c = 0, 0,0
        res = 0

        count = 0
        while (a or b) and count < BIT_COUNT + 1:
            i = a & 1
            j = b & 1
            v,c = calc(i,j,c)

            res |= v << count

            a >>= 1
            b >>= 1
            count += 1

        if count < BIT_COUNT + 1:
            # final carry
            v, _ = calc(0,0,c)
            res |= v << count

        if res >> BIT_COUNT:
            res = ~((((1 << BIT_COUNT) - 1) & ~res) + 1) + 1
        return res
    
    