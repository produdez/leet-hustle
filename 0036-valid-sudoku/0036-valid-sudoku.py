class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            Version 1:
                Naive check all rows/cols/square using HashSet
                Complexity: Given n as board size (fixed 9 in this case)
                - Time: O(n^2) (cus checking dup and adding dup takes O(1)
                - Space: O(n *(3n)) -> O(n^2)
                    3 sets of size n for each (row/col/square)
                    -> n * (3n)
        '''
        def hasDuplicate(val, dup):
            if val == '.': return False
            if val in dup: return True
            dup.add(val)
            return False

        for i in range(9):
            dup_row, dup_col, dup_square = set(), set(), set()
            for j in range(9):
                if hasDuplicate(board[i][j], dup_row): return False
                if hasDuplicate(board[j][i], dup_col): return False
                if hasDuplicate(
                    board[(i//3)*3 + j//3][(i%3)*3 + j%3], 
                    dup_square
                ): return False
        return True