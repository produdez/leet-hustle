class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
            Translate from int (2's compliment) to one's complement
            
            Do calculation based on one's complement
            
            Translate back to two's complement
            
            Better approach is to learn how to do 2's complement (todo later)
            toOne and toTwo should (could?) be one function
        '''
        
        
        MAX_INT = 0b11111111111 # one extra for sign and 10 for value since max is 1000
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
        
        
        def toOne(i):
            if i > 0: return i
            return MAX_INT & (i - 1)

        def toTwo(c1):
            if c1.bit_length() < MAX_INT.bit_length(): return c1
            return int('-'+bin(MAX_INT & ~c1),2) # Un-optimized



        def sum1c(a,b):
            c = 0
            # one extra redundant bit
            res = 1 << MAX_INT.bit_length()
            
            for count in range(MAX_INT.bit_length()):
                i = a%2
                j = b%2

                v, c = lookupTable[(i,j,c)]
                res |= v << count
                a >>= 1
                b >>= 1

            # remove bit at head
            res = res ^ (1 << (res.bit_length() - 1)) 
            
            # must be a recursive call since we must run though all bits to know if carry stays
            # might try an initialized while loop but fuck you bitHC as bit manupluatioavhasgfbalweuvvr,zdvasefez
            if c: return sum1c(res,c) 
            return res
        
        oneComplimentResult = sum1c(toOne(a), toOne(b))
        return toTwo(oneComplimentResult)