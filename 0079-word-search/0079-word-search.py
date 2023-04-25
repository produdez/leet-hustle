class Solution:
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
            
        def next_valid_positions(path):
            if len(path) < 1:
                starting_pos = []
                for i in range(len(board[0])):
                    for j in range(len(board)):
                        if board[j][i] == word[0]: starting_pos.append((i,j))
                return starting_pos
            
            if len(path) >= len(word): return []
            
            cur_x, cur_y = path[-1]
            next_poses = []
            for dx, dy in POS_MOVES:
                new_x, new_y = cur_x + dx, cur_y + dy
                
                # boundary check
                if new_x < 0 or new_x >= len(board[0]): continue
                if new_y < 0 or new_y >= len(board): continue
                
                # check matching character
                if board[new_y][new_x] != word[len(path)]: continue
                
                # check repeated backtrack
                if (new_x, new_y) in path: continue
                
                next_poses.append((new_x, new_y))
            return next_poses

        def backtrack(path = []):
            next_poses = next_valid_positions(path)
            if not next_poses and len(path) == len(word):
                return True
            # print('next to try: ', next_poses)
            for next_pos in next_poses:
                path.append(next_pos)
                if backtrack(path): return True
                path.pop()
            return False
        # print_board(board)
        # print('word: ', word)
        
        if set(word) - set([i for row in board for i in row]): return False
        return backtrack()