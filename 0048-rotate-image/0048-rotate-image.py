class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
            Simple approach with updated rotate mechanism
            1. Traverse a quadrant of the matrix
            2. Repeat 4 times the rotation (cause there's 4 quadrants)
            3. Rotation include:
                a. translate the index to relative to the center
                b. rotate using math formula
                c. translate back to original index
        """
        
        n = len(matrix)
        
        def translate(pos, origin, new_origin):
            transpose_vector = (origin[0] - new_origin[0], origin[1] - new_origin[1])
            new_pos = (pos[0] + transpose_vector[0], pos[1] + transpose_vector[1])
            return new_pos    

        def rotate(pos):
            t_pos = translate(pos, origin, center)
            # y, -x is rot 90 clock wise with x points down and y points right
            t_rotated = (t_pos[1], -t_pos[0]) 
            rotated = translate(t_rotated, center, origin)
            return int(rotated[0]), int(rotated[1])
        
        
        def get(grid, pos):
            return grid[pos[0]][pos[1]]
        
        def first_quadrant():
            offset = n%2 # add one more row in case of odd n
            for i in range(n//2 + offset):
                for j in range(n//2):
                    yield (i,j)
        
        origin = (0,0)
        center = ((n-1)/2, (n-1)/2)
        for cur in first_quadrant():
            cur_val = get(matrix, cur)
            if cur == center: continue

            for _ in range(4):
                nxt = rotate(cur)
                temp = get(matrix, nxt)
                matrix[nxt[0]][nxt[1]] = cur_val
                
                cur = nxt
                cur_val = temp
        
