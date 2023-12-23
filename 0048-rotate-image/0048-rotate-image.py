class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        ROTATE_TABLE = {
            (-1, -1):   (-1, 1),
            (-1, 1) :   (1, 1),
            (1, 1)  :   (1, -1),
            (1, -1) :   (-1, -1),
        }
        
        def translate(pos, origin, new_origin):
            transpose_vector = (origin[0] - new_origin[0], origin[1] - new_origin[1])
            new_pos = (pos[0] + transpose_vector[0], pos[1] + transpose_vector[1])
            return new_pos    

        def rotate(pos):
            t_pos = translate(pos, origin, center)
            # rotation logic (relative to translated center)
            x,y = t_pos
            sx = 1 if x > 0 else -1 # s is sign
            sy = 1 if y > 0 else -1
            
            new_sx, new_sy = ROTATE_TABLE[(sx, sy)]
            
            # swap x,y and include their new sign
            t_rotated = (abs(y) * new_sx, abs(x) * new_sy) 
            rotated = translate(t_rotated, center, origin)
            # print(f'pos: {pos}, t_pos: {t_pos}, t_rotated: {t_rotated}, rotated: {rotated}')
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
        # print('CENTER: ', center)
        for cur in first_quadrant():
            # print('--quadrant pos: ', cur)
            cur_val = get(matrix, cur)
            if cur == center: continue

            for _ in range(4):
                nxt = rotate(cur)
                # print('cur: ', cur, 'rotated: ', nxt)
                temp = get(matrix, nxt)
                matrix[nxt[0]][nxt[1]] = cur_val
                
                cur = nxt
                cur_val = temp
        
