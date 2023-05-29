class Solution:
    
    def numDecodings(self, s: str) -> int:
        memoize = {}
        def valid(char):
            
            if not char or char[0] == '0': return False
            
            num = int(char)
            res = num > 0 and num <= 26
            # print('validating: ', char, res)
            return res
        
        def countDec(start):
            # print('counting: ', s[start:], ' start: ', start)
            if start in memoize: return memoize[start]
            
            if start == len(s):
                total = 1
            elif start < len(s):
                total = 0
                if valid(s[start]): total += countDec(start+1)
                if valid(s[start: start+2]): total += countDec(start+2)
            else:
                total = 0 
            # print('total: ', total)
            memoize[start] = total
            return total
        
        
        return countDec(0)
        