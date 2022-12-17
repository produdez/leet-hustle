class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
            Solution
            
            - Idea:
                Have a container that represents the zig-zag patterns (rows)
                And a counter that changes zig-zagly
                Keep appending to the correct row and collect results at the end
            - Time complexity:
                1. Loop the string O(n)
                2. Loop and join the rows O(n)
                => total O(2n) = O(n)
            - Space complexity: mainly the container
                O(n) or O(numRows * M) with M being the average size of each rows
        '''
        container = ['' for _ in range(numRows)]
        
        counter = 0
        increment = -1 if numRows > 1 else 0
        for char in s:
            container[counter] += char
            
            if counter == 0 or counter == numRows - 1: increment = -increment
            counter = counter + increment
        
        return ''.join(container)