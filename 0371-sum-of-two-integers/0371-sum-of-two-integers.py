class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
            Implement 2's complement sum
        '''


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

        BIT_COUNT = 10

        i,j,c = 0, 0,0
        res = 0 # extra place hold bit
        # print('---------------')
        # print('starting: ', a,b)
        # print('init res: ', bin(res))
        count = 0
        while (a or b) and count < BIT_COUNT + 1:
            i = a & 1
            j = b & 1

            # print('i,j,c: ', i,j,c)
            v, c = lookupTable[(i,j,c)]

            # print('v,c: ', v,c)
            res |= v << count

            # print('res: ', res, bin(res))

            a >>= 1
            b >>= 1
            count += 1

        # print('final count: ', count)
        if count < BIT_COUNT + 1:
            # print('final adjust')
            v, _ = lookupTable[(0,0,c)] # final carry
            res |= v << count


        # print('final result: ', res, bin(res))
        if res >> BIT_COUNT:
            res = ~((0b11111111111 & ~res) + 1) + 1
        return res
    
    