class Solution:
    def romanToInt(self, s: str) -> int:
        romanVal = {
            'I'      :       1,
            'V'       :      5,
            'X'        :     10,
            'L'         :    50,
            'C'          :   100,
            'D'           :  500,
            'M'            : 1000
        }
        
        prevVal = 9999
        total = 0
        for char in s:
            val = romanVal.get(char)
            if prevVal < val: total += (val - 2 * prevVal)
            else: total += val
            prevVal = val
        return total
        