class Solution:
    def convert(self, s: str, numRows: int) -> str:
        container = [[] for _ in range(numRows)]
        
        counter = 0
        increment = -1 if numRows > 1 else 0
        for char in s:
            container[counter].append(char)
            
            if counter == 0 or counter == numRows - 1: increment = -increment
            counter = counter + increment
        
        return ''.join([''.join(arr) for arr in container])