class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            Version 2
            
            Idea:
                Same idea, gen all cases
                But now uses backtracking approach (DFS)
                and possibly less space
            Complexity:
                = Tree size
        '''
        
        stack = [] # this stack keeps track of the current result we're building
        result = []
        def backtrack(l, r):
            if l == r == n: 
                result.append(''.join(stack))

            if l >= r and l < n:
                stack.append('(')
                backtrack(l+1, r)
                stack.pop()
            
            if r < n:
                stack.append(')')
                backtrack(l, r+1)
                stack.pop()
        
        backtrack(0,0)
        return result
                