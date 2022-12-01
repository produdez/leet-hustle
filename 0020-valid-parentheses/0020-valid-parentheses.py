class Solution:
    '''
        Idea: Have a stack to push non-closed left bracket into
            - When encounter a right bracket, pop the stack and check valid
        Notable case:
            - Stack empty (means not enough open bracket) -> False
            - Empty string -> True
            - Stack not empty at the end (means not enough close bracket) -> False
    '''
    def matches(self, left, right):
        if left == '(' and right == ')': return True
        if left == '[' and right == ']': return True
        if left == '{' and right == '}': return True
        return False
    
    def isLeft(self, c): return c in ['(', '[', '{']
    def isRight(self, c): return c in [')', ']', '}'] # ! unused

    def isValid(self, s: str) -> bool:
        stack = [] # should be a stack
        for char in s:
            if self.isLeft(char): 
                stack.append(char)
            else:
                if len(stack) is 0: return False
                lastLeft = stack.pop()
                if not self.matches(lastLeft, char): return False
        return len(stack) is 0