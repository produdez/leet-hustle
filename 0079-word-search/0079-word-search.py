class Solution:
    '''
        Version: 2
            Update to use set for faster checking
            (STILL NOT EFFICIENT ENOUGH)
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        POS_MOVES = [
            (1, 0), # right
            (0, -1), # down
            (-1, 0), # left
            (0, 1), # up
        ]

        def print_board(board):
            ender = '---------'
            print(ender)
            for line in board:
                for char in line:
                    print(char, end=', ')
                print()
            print(ender)

        def next_valid_positions(path, cur):
            if len(path) < 1:
                total_board_size = len(board) * len(board[0])
                i = 0
                while i < total_board_size:
                    if board[i // len(board[0])][i % len(board[0])] == word[0]:
                        yield i
                    i += 1
                return

            if len(path) >= len(word): return
            
            cur_x, cur_y = cur % len(board[0]), cur // len(board[0])
            for dx, dy in POS_MOVES:
                new_x, new_y = cur_x + dx, cur_y + dy
                
                # boundary check
                if new_x < 0 or new_x >= len(board[0]): continue
                if new_y < 0 or new_y >= len(board): continue
                
                # check matching character
                if board[new_y][new_x] != word[len(path)]: continue
                
                new_idx = new_y * len(board[0]) + new_x
                # check repeated backtrack
                if new_idx in path: continue
                
                yield new_idx
            return

        def backtrack(path = set(), cur = None):
            for next_pos in next_valid_positions(path, cur):
                path.add(next_pos)
                if backtrack(path, next_pos): return True
                path.remove(next_pos)
            
            if len(path) == len(word): return True
            return False

        
        if set(word) - set([i for row in board for i in row]): return False
        return backtrack()