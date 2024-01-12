class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        l,r,t,b = 0, m, 0, n
        
        result = []
        while True: # intend that border is last index + 1
            
            # top
            if t >= b: break
            i = t
            for j in range(l, r):
                result.append(matrix[i][j])
            t += 1
            
            # right
            if l >= r: break
            j = r - 1
            for i in range(t, b):
                result.append(matrix[i][j])
            r -= 1
            
            # bot
            if t >= b: break
            i = b - 1
            for j in reversed(range(l, r)):
                result.append(matrix[i][j])
            b -= 1
            
            # left
            if l >= r: break
            j = l
            for i in reversed(range(t, b)):
                result.append(matrix[i][j])
            l += 1
        
        return result
            