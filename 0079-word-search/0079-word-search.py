class Solution:
    '''
        Version: 3
            Mod the board directly
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

        def next_valid_positions(cur, path_len):
            if not cur or path_len == 0:
                for j in range(len(board)):
                    for i in range(len(board[0])):
                        if board[j][i] == word[0]: yield (i,j)
                return

            if path_len >= len(word): return
            
            cur_x, cur_y = cur
            for dx, dy in POS_MOVES:
                new_x, new_y = cur_x + dx, cur_y + dy
                
                # boundary check
                if new_x < 0 or new_x >= len(board[0]): continue
                if new_y < 0 or new_y >= len(board): continue
                
                # check matching character
                if board[new_y][new_x] != word[path_len]: continue
                
                # check repeated backtrack
                if board[new_y][new_x] == '#': continue
                
                yield (new_x, new_y)
            return

        def backtrack(cur = None, path_length = 0):
            for next_x, next_y in next_valid_positions(cur, path_length):
                temp = board[next_y][next_x]
                board[next_y][next_x] = '#'
                if backtrack((next_x, next_y), path_length + 1): return True
                board[next_y][next_x] = temp
            
            if path_length == len(word): return True
            return False

        
        # if set(word) - set([i for row in board for i in row]): return False
        return backtrack()