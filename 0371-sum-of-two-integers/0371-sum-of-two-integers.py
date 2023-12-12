class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0b11111111111
        def toOne(i):
            if i > 0: return i
            return MAX_INT & (i - 1)

        def toTwo(c1):
            if c1.bit_length() < MAX_INT.bit_length(): return c1
            return int('-'+bin(MAX_INT & ~c1),2)


        lookupTable = {
            (1,1,1): (1,1),
            (1,1,0): (0,1),

            (0,1,0): (1,0),
            (1,0,0): (1,0),

            (0,1,1): (0,1),
            (1,0,1): (0,1),

            (0,0,0): (0,0),
            (0,0,1): (1,0),
        }
        def sum1c(a,b):

            c = 0
            # one extra redundant bit
            res = 1 << MAX_INT.bit_length()
            for count in range(res.bit_length() - 1):
                i = a%2
                j = b%2
                # print('count: ', count)
                # print(f'i-{i}, j-{j}, c-{c}')
                v, c = lookupTable[(i,j,c)]
                res |= v << count
                # print('v-',v,'-res: ', bin(res))
                a //= 2
                b //= 2

            res = res ^ (1 << (res.bit_length() - 1))
            # print('after clear msb res: ', bin(res))
            if c:
                # print('last carry')
                return sum1c(res, c)
            return res
        
        oneComplimentResult = sum1c(toOne(a), toOne(b))
        return toTwo(oneComplimentResult)