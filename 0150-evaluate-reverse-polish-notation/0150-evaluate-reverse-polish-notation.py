class Solution:
    '''
        Version: 2
            Simpler code, eliminate wasted if checks
            + Push the converted value in so that we dont need to convert when pop
        Idea: Push pending values to a stack, pop out when see an operator
            Calculate and push back into stack
        Complexity:
            Time: O(n)
            Space: O(n)
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        wait = []
        for token in tokens:
            match token:
                case '+': wait.append(wait.pop() + wait.pop())
                case '-': 
                    r, l = wait.pop(), wait.pop()
                    wait.append(l - r)
                case '*': wait.append(wait.pop() * wait.pop())
                case '/': 
                    r, l = wait.pop(), wait.pop()
                    wait.append(int(l/r))
                case _:
                    wait.append(int(token))
        
        return int(wait[0])