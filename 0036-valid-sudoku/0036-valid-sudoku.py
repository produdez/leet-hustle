class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            Version 1.5: Update simpler code and probably better performance
                upda
                Naive check all rows/cols/square using HashSet
                Complexity: Given n as board size (fixed 9 in this case)
                
                >>
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.': continue

                if val in rows[i]: return False
                if val in cols[j]: return False
                if val in squares[(i//3, j//3)]: return False
                
                rows[i].add(val)
                cols[j].add(val)
                squares[(i//3, j//3)].add(val)
        return True