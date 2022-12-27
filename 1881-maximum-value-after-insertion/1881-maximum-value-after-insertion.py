class Solution:
    def maxValue(self, n: str, x: int) -> str:
        negative = n[0] == '-' 
        sign = -1 if negative else 1
        start = 1 if negative else 0

        insert_index = len(n)
        for i, char in enumerate(n[1:] if negative else n):
            digit = int(char) * sign
            if x*sign > digit: 
                insert_index = i
                break
            
        return n[:insert_index+start] + str(abs(x)) + n[insert_index+start:]