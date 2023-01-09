class Solution:
    '''
        Version: 1
        Idea: Push pending values to a stack, pop out when see an operator
            Calculate and push back into stack
        Complexity:
            Time: O(n)
            Space: O(n)
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        wait = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                wait.append(token)
                continue
            
            right = int(wait.pop())
            left = int(wait.pop())
            match token:
                case '+': wait.append(left + right)
                case '-': wait.append(left - right)
                case '*': wait.append(left * right)
                case '/': wait.append(left/right)
        
        return int(wait[0])