class Solution:
    '''
        Version: 1.5
            Same as version 1 
            but slight cleaner backtrack code
            and uses generator
        Same efficient and space when summited
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        POS_MOVES = [
            (1, 0), # right
            (0, -1), # down
            (-1, 0), # left
            (0, 1), # up
        ]
            
        def next_valid_positions(path):
            if len(path) < 1:
                for i in range(len(board[0])):
                    for j in range(len(board)):
                        if board[j][i] == word[0]: yield (i,j)
                return

            if len(path) >= len(word): return
            
            cur_x, cur_y = path[-1]
            for dx, dy in POS_MOVES:
                new_x, new_y = cur_x + dx, cur_y + dy
                
                # boundary check
                if new_x < 0 or new_x >= len(board[0]): continue
                if new_y < 0 or new_y >= len(board): continue
                
                # check matching character
                if board[new_y][new_x] != word[len(path)]: continue
                
                # check repeated backtrack
                if (new_x, new_y) in path: continue
                
                yield (new_x, new_y)
            return

        def backtrack(path = []):
            for next_pos in next_valid_positions(path):
                path.append(next_pos)
                if backtrack(path): return True
                path.pop()
            
            if len(path) == len(word): return True
            return False

        
        if set(word) - set([i for row in board for i in row]): return False
        return backtrack()