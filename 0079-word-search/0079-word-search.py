class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        def dfs(i, j, k):
            # i, j is location in the grid
            # k is word index
            if k >= len(word): return False
            if i <0 or j <0: return False
            if i >= len(board) or j >= len(board[0]): return False
            if (i,j) in path: return False
            if board[i][j] != word[k]: return False
            path.add((i,j))
            # try the 4 other paths
            result = False
            if k == len(word) - 1: 
                result = True
            elif (dfs(i+1, j, k+1) or
            dfs(i-1, j, k+1) or
            dfs(i, j+1, k+1) or
            dfs(i, j-1, k+1)):
                result = True
            
            path.remove((i,j))
            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0): return True
        return False