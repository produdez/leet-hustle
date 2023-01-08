class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
                if hasDuplicate(board[(i//3)*3 + j//3][(i%3)*3 + j%3], dup_square): 
                    return False
        return True